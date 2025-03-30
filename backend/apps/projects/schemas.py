# @Time：2025/3/26 09:57
# @Author：jinglv
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

from apps.users.schemas import UserInfoResponse


# =====================================项目相关的数据模型=================================
class CreateProjectFormRequest(BaseModel):
    """
    添加项目
    """
    name: str = Field(description="项目名称", max_length=20)
    user: int = Field(description="项目负责人")
    description: str = Field(description="项目描述")


class UpdateProjectFormRequest(BaseModel):
    """
    更新项目
    """
    name: str = Field(description="项目名称", max_length=20)
    description: str = Field(description="项目描述")


class ProjectResponse(BaseModel):
    """
    项目详情
    """
    id: int = Field(description="项目id")
    name: str = Field(description="项目名称")
    user: UserInfoResponse
    description: str = Field(description="项目描述")
    # 时间在声明的时候要注意类型
    create_time: datetime = Field(description="创建时间")


class ProjectPageListResponse(BaseModel):
    """
    分页获取项目列表
    """
    total: int = Field(description="总数")
    data: List[ProjectResponse] = Field(description="数据")
