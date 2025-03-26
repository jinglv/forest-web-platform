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

# ==========================token的配置=====================================
# 64位秘钥
SECRET_KEY = "8beac45e868942b7157e25a0396f36db16ea92dd6713c9ebd116c5259e3fb3d3"
# 加密算法
ALGORITHM = "HS256"
# token过期时间
TOKEN_TIMEOUT = 60 * 60 * 24 * 7
