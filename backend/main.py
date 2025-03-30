# @Time：2025/3/19 16:26
# @Author：jinglv
import time

import uvicorn
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError, HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from tortoise.contrib.fastapi import register_tortoise

from apps.projects.api import router as project_router
from apps.users.api import router as user_router
from common.settings import TORTOISE_ORM

app = FastAPI(title="Forest Web测试平台", version="1.0.0", description="FastAPI")

# ==================注册ORM模型==================
register_tortoise(app, config=TORTOISE_ORM, modules={"models": ["models"]})


# ==================自定义全局异常处理==================
@app.exception_handler(RequestValidationError)
def request_validation_exception_handler(request, exc):
    """
    自定义全局请求参数校验异常处理
    :param request:
    :param exc:
    :return:
    """
    return JSONResponse(
        status_code=400,
        content={"code": 400, "msg": "请求参数校验失败", "data": None, "error": str(exc)}
    )


@app.exception_handler(HTTPException)
def http_exception_handler(request, exc):
    """
    自定义全局HTTP异常处理
    :param request:
    :param exc:
    :return:
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": exc.status_code, "msg": exc.detail, "data": None, "error": None}
    )


# =================跨域请求的支持==================
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =================自定义请求响应中间件==================
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # 调用处理函数之前
    start_time = time.time()
    # 调用处理函数
    response = await call_next(request)
    # 调用处理函数之后
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# =================注册路由==================
app.include_router(user_router)
app.include_router(project_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
