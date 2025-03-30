# @Time：2025/3/26 09:57
# @Author：jinglv

from tortoise import models, fields


class ProjectsModel(models.Model):
    """
    项目表
    """
    id = fields.IntField(description="项目id", primary_key=True)
    name = fields.CharField(max_length=50, description="项目名称")
    description = fields.CharField(max_length=255, default="", description="项目描述")
    user = fields.ForeignKeyField('models.UsersModel', description="项目负责人", related_name="project")
    create_time = fields.DatetimeField(auto_now_add=True, description="创建日期")
    updated_time = fields.DatetimeField(auto_now=True, description="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        table = "forest_projects"
        table_description = "项目表"


class EnvsModel(models.Model):
    """
    环境表
    """
    id = fields.IntField(description="环境id", primary_key=True)
    project = fields.ForeignKeyField('models.ProjectsModel', description="所属项目", related_name="envs")
    global_variable = fields.JSONField(description="全局变量", default=dict, null=True, blank=True)
    name = fields.CharField(description="测试环境名称", max_length=50)
    host = fields.CharField(description="测试环境的host地址", max_length=50)
    create_time = fields.DatetimeField(auto_now_add=True, description="创建日期")
    updated_time = fields.DatetimeField(auto_now=True, description="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        table = "forest_envs"
        table_description = "环境表"


class ProjectModuleModel(models.Model):
    """
    功能模块表
    """
    id = fields.IntField(description="模块id", primary_key=True)
    name = fields.CharField(max_length=50, description="模块名称")
    project = fields.ForeignKeyField('models.ProjectsModel', description="所属项目", related_name="modules")
    create_time = fields.DatetimeField(auto_now_add=True, description="创建日期")
    updated_time = fields.DatetimeField(auto_now=True, description="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        table = "forest_project_module"
