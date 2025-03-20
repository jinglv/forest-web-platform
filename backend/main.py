# @Time：2025/3/19 16:26
# @Author：jinglv
import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from apps.users.api import router as user_router
from common.settings import TORTOISE_ORM

app = FastAPI()

# 注册ORM模型
register_tortoise(app, config=TORTOISE_ORM, modules={"models": ["models"]})

# 注册路由
app.include_router(user_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
