# forest-web-platform服务端

## 技术栈

- Python 3.13.2
- FastApi
- Tortoise

## 项目结构

```
project_root/

├── README.md
├── apps
│   └── users
│       ├── api.py		# api定义
│       ├── models.py		# 数据模型
│       └── schemas.py	# Pydantic 模型
|   └── projects
│       ├── api.py
│       ├── models.py
│       └── schemas.py
| ...
├── common					# 公共配置和方法
│   └── settings.py
├── main.py					# 应用启动文件
├── migrations				# 存放迁移记录
├── pyproject.toml			# 项目管理配置
├── requirements.txt		# 依赖库列表
├── tests					# 测试代码

```

## 数据库迁移命令

创建数据库

```mysql
DROP DATABASE IF EXISTS `forest_web_test`;
CREATE DATABASE `forest_web_test` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
```

- 在项目根目录下运行以下命令

  ```
  aerich init -t main.TORTOISE_ORM
  ```

  其中 `app.TORTOISE_ORM` 是 Tortoise ORM 的配置路径。例如，如果 Tortoise 配置在 `main.py` 中，配置路径可以是
  `main.TORTOISE_ORM`。

  执行完成后，项目目录下会生成一个`migrations`目录(用于存放迁移记录)和`pyproject.toml`文件

- 生成迁移文件，初始化 数据库

  ```
  aerich init-db
  ```

- 每次修改模型后，运行以下命令生成迁移文件

  ```
  aerich migrate
  ```


- 应用迁移

  ```
  aerich upgrade
  ```

## 项目运行步骤

1. 生成迁移配置文件：aerich init -t main.TORTOISE_ORM
2. 执行迁移：aerich init-db(第一次)
3. 数据库模型后续变动：
    - 更新迁移文件：aerich migrate
    - 执行最近的迁移文件：aerich upgrade
4. 启动项目，通过fastapi自带的运行工具
    - 开发环境：fastapi dev main.py
    - 生产环境：fastapi run main.py

## Websocket接口

安装依赖： `pip install websockets`

```python
from fastapi import APIRouter, FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect

app = FastAPI()
router = APIRouter()


# ws://127.0.0.1:8000/ws

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # 等待客户端简历连接
    await websocket.accept()
    try:
        while True:
            # 读取客户端传递到的数据
            data = await websocket.receive_text()
            print(f"接收到消息：{data}")
            # 返回数据给客户端
            await websocket.send_json({"code": 100, "msg": "ok", "data": "Hello, World!"})
    except WebSocketDisconnect as e:
        # 客户端断开连接
        print(f"客户端断开连接：{e}")
        await websocket.close()


# 注册路由
app.include_router(router)
```

## 依赖注入

FastAPI 有一个非常强大但直观的依赖注入系统，在路由的处理函数(视图中)有一种方法来声明它工作和使用所需的东西：“依赖关系”。
以为您的代码添加依赖项。主要应用在以下场景上：

- 具有共享逻辑
- 共享数据库连接。
- 强制执行安全性、身份验证、角色要求等。
- 还有很多其他的事情......

案例：有多个api需要定义一样的参数，可以将参数的定义单独拿出来作为一个依赖进行注入。

```python
from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, page: int = 0, size: int = 100):
    return {"q": q, "page": page, "size": size}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons
```

每当有新请求到达时，FastAPI 都会处理：

- 使用正确的参数调用依赖项 Depends（“common_parameters”） 函数。
- 从函数中获取结果。
- 将该结果分配给路径运算函数中的参数。

这样，只需编写一次共享代码，FastAPI 就会负责为路径操作调用它。