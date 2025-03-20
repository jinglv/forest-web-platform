# @Time：2025/3/19 16:26
# @Author：jinglv
from tortoise import models, fields


class UsersModel(models.Model):
    """
    用户模型
    """
    id = fields.IntField(pk=True, auto_increment=True, description="用户id")
    username = fields.CharField(max_length=255, description="用户名")
    password = fields.CharField(max_length=255, description="密码")

    def __str__(self):
        return self.username

    class Meta:
        table = "users"
        table_description = "用户表"
