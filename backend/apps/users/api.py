# @Time：2025/3/19 16:26
# @Author：jinglv
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from apps.users.models import UsersModel
from apps.users.schemas import RegisterFormRequest, UserInfoResponse, LoginResponse, LoginFormRequest, TokenRequest, \
    Token
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
        raise HTTPException(status_code=422, detail="两次密码不一致")
    # 判断用户名是否已存在
    if await UsersModel.get_or_none(username=request.username):
        raise HTTPException(status_code=422, detail="用户名已存在")
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
    登录的逻辑,实现用户名、手机号、邮箱均可以作为账号登录
    :param request:
    :return:
    """
    user_name = await UsersModel.get_or_none(username=request.username)
    user_mobile = await UsersModel.get_or_none(mobile=request.username)
    user_email = await UsersModel.get_or_none(email=request.username)
    user = user_name or user_mobile or user_email
    if not user:
        raise HTTPException(status_code=422, detail="用户名或密码错误")
    if not user_auth.verify_password(request.password, user.password):
        raise HTTPException(status_code=422, detail="用户名或密码错误")
    uinfo = UserInfoResponse(**user.__dict__)
    # 账户名密码正确，生成token
    token = user_auth.create_token(uinfo.model_dump())
    # 返回token 和用户信息
    return LoginResponse(token=token, user=uinfo)


@router.post("/verify", summary="校验token", response_model=UserInfoResponse)
def verify_token(request: TokenRequest):
    """
    校验token
    :param request: 请求信息
    :return:
    """
    return user_auth.verify_token(request.token)


@router.post("/refresh", summary="刷新token", response_model=TokenRequest)
def refresh_token(request: TokenRequest):
    """
    刷新token
    :param request: 请求信息
    :return:
    """
    # 校验token,获取token中的用户信息
    userinfo = user_auth.verify_token(request.token)
    # 生成新的token
    return {"token": user_auth.create_token(userinfo)}


@router.post("/token", response_model=Token, tags=["API调试"], summary="模拟登录")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    给接口文档登录生成token的api
    :param form_data:
    :return:
    """
    user = await UsersModel.get_or_none(username=form_data.username)
    if not user:
        raise HTTPException(status_code=422, detail="用户名或密码错误")
    if not user_auth.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=422, detail="用户名或密码错误")
    uinfo = UserInfoResponse(**user.__dict__)
    token = user_auth.create_token(uinfo.model_dump())
    return Token(access_token=token, token_type="bearer")
