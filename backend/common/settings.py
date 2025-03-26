# @Time：2025/3/19 16:32
# @Author：jinglv

# =========================数据库的配置信息=======================
DATABASE = {
    'host': 'localhost',
    'port': '3306',
    'user': 'root',
    'password': '123456',
    'database': 'forest_web_test',
}

# 项目中的所以应用的models
INSTALLED_APPS = [
    'apps.users.models',
]
# 关于tortoise的配置
TORTOISE_ORM = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': DATABASE
        },
    },
    'apps': {
        'models': {
            'models': ['aerich.models', *INSTALLED_APPS],  # 模型类所在的包名
            'default_connection': 'default',
        },
    }
}
