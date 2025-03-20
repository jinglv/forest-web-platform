# @Time：2025/3/19 16:27
# @Author：jinglv
from pydantic import BaseModel, Field


class LoginForm(BaseModel):
    username: str = Field(description="用户名", min_length=6, max_length=20)
    password: str = Field(description="密码", min_length=6, max_length=18)
