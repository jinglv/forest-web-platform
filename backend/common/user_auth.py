# @Time：2025/3/26 14:56
# @Author：jinglv
"""
用户认证和权限校验的公共模块
pip install pyjwt
pip install passlib[bcrypt]
"""
import secrets
import time

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from common import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/token")


async def is_authenticated(token: str = Depends(oauth2_scheme)) -> dict:
    """
    校验token中的用户信息
    :param token:
    :return:
    """
    return verify_token(token)


def create_token(userinfo: dict):
    # 过期时间
    expire = int(time.time()) + settings.TOKEN_TIMEOUT
    userinfo['exp'] = expire
    # 使用pyjwt生成token
    return jwt.encode(userinfo, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def verify_token(token):
    """
    校验token
    :param token:
    :return:
    """
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        return data
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="token校验失败或者无效token")
    except Exception as e:
        raise HTTPException(status_code=401, detail="错误token")


def verify_password(plain_password, hashed_password):
    """
    校验密码
    :param plain_password: 明文密码
    :param hashed_password: 密文密码
    :return:
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """
    哈希密码
    :param password: 明文密码
    :return:
    """
    return pwd_context.hash(password)


def generate_secret_key():
    """
    生成密钥
    :return:
    """
    return secrets.token_hex(64)
