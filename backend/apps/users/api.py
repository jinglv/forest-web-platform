# @Time：2025/3/19 16:26
# @Author：jinglv
from fastapi import APIRouter, HTTPException

from apps.users.models import UsersModel
from apps.users.schemas import RegisterFormRequest, UserInfoResponse, LoginResponse, LoginFormRequest
from common import user_auth

router = APIRouter(prefix="/api/users", tags=['用户模块'])


@router.post('/register', response_model=UserInfoResponse, summary='用户注册')
async def register(request: RegisterFormRequest):
    """
    用户注册接口
    :param request: 请求参数
    :return:
    """
    # 判断密码是否一致
    if request.password != request.password_confirm:
        return HTTPException(status_code=422, detail="两次密码不一致")
    # 判断用户名是否已存在
    if await UsersModel.get_or_none(username=request.username):
        return HTTPException(status_code=422, detail="用户名已存在")
    # 校验邮箱是否已存在
    if await UsersModel.get_or_none(email=request.email):
        raise HTTPException(status_code=422, detail="邮箱已存在")
    # 校验手机号是否已存在
    if await UsersModel.get_or_none(mobile=request.mobile):
        raise HTTPException(status_code=422, detail="手机号已存在")
    # 生成一个密文的密码
    hash_pwd = user_auth.get_password_hash(request.password)
    # 注册
    user = await UsersModel.create(
        username=request.username,
        password=hash_pwd,
        email=request.email,
        mobile=request.mobile,
        nickname=request.nickname,
    )
    return UserInfoResponse(**user.__dict__)


@router.post('/login', response_model=LoginResponse, summary='用户登录')
async def login(request: LoginFormRequest):
    """
    用户登录接口
    :param request:
    :return:
    """
    user = await UsersModel.get_or_none(username=request.username)
    if not user:
        raise HTTPException(status_code=422, detail="用户名或密码错误")
    if not user_auth.verify_password(request.password, user.password):
        raise HTTPException(status_code=422, detail="用户名或密码错误")
    uinfo = UserInfoResponse(**user.__dict__)
    # 账户名密码正确，生成token
    token = user_auth.create_token(uinfo.dict())
    # 返回token 和用户信息
    return LoginResponse(token=token, user=uinfo)
