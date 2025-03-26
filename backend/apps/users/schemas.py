# @Time：2025/3/19 16:27
# @Author：jinglv
from pydantic import BaseModel, Field


class LoginFormRequest(BaseModel):
    username: str = Field(description="用户名", min_length=6, max_length=20)
    password: str = Field(description="密码", min_length=6, max_length=18)


class RegisterFormRequest(LoginFormRequest):
    password_confirm: str = Field(description="确认密码", min_length=6, max_length=18)
    email: str = Field(description="邮箱")
    mobile: str = Field(description="手机号")
    nickname: str = Field(default='', description="昵称")


class UserInfoResponse(BaseModel):
    id: int = Field(description="用户id")
    username: str = Field(description="用户名")
    nickname: str = Field(description="昵称")
    email: str = Field(description="邮箱")
    mobile: str = Field(description="手机号")
    is_active: bool = Field(description="是否激活")
    is_superuser: bool = Field(description="是否超级管理员")


class LoginResponse(BaseModel):
    token: str = Field(description="访问令牌")
    user: UserInfoResponse


class TokenRequest(BaseModel):
    token: str = Field(description="访问令牌")


class Token(BaseModel):
    """
    接口文档的使用的
    """
    access_token: str
    token_type: str
