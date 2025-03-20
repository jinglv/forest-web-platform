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
│       ├── api.py			# api定义
│       ├── models.py		# 数据模型
│       └── schemas.py	# Pydantic 模型
|   └── projects
│       ├── api.py
│       ├── models.py
│       └── schemas.py
| ...
├── common							# 公共配置和方法
│   └── settings.py
├── main.py							# 应用启动文件
├── migrations					# 存放迁移记录
├── pyproject.toml			# 项目管理配置
├── requirements.txt		# 依赖库列表
├── tests								# 测试代码

```



## 数据库迁移命令

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