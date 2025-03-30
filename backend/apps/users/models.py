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
    nickname = fields.CharField(max_length=255, description="用户昵称")
    email = fields.CharField(max_length=255, description="邮箱", default="")
    mobile = fields.CharField(max_length=255, description="手机号", default="")
    is_active = fields.BooleanField(default=True, description="是否激活")
    is_superuser = fields.BooleanField(default=False, description="是否超级管理员")
    created_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    updated_time = fields.DatetimeField(auto_now=True, description="更新时间")

    def __str__(self):
        return self.username

    class Meta:
        table = "forest_users"
        table_description = "用户表"
