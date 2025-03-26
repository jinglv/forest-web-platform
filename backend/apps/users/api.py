# @Time：2025/3/19 16:26
# @Author：jinglv
from fastapi import APIRouter, HTTPException

from apps.users.models import UsersModel
from apps.users.schemas import RegisterFormRequest, UserInfoResponse

router = APIRouter(prefix="/api/users", tags=['用户模块 '])


@router.post('/register', response_model=UserInfoResponse, summary='用户注册')
async def register(request: RegisterFormRequest):
    """
    用户注册接口
    :param request: 请求参数
    :return:
    """
    # 判断密码是否一致
    if request.password != request.password_confirm:
        return HTTPException(status_code=400, detail="两次密码不一致")
    # 判断用户名是否已存在
    if await UsersModel.get_or_none(username=request.username):
        return HTTPException(status_code=400, detail="用户名已存在")
    # 进行注册
    user = await UsersModel.create(**request.model_dump())
    return UserInfoResponse(**user.__dict__)
