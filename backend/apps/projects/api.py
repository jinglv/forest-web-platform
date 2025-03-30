# @Time：2025/3/26 09:57
# @Author：jinglv

from fastapi import APIRouter, HTTPException, Depends

from apps.projects.models import ProjectsModel
from apps.projects.schemas import ProjectResponse, CreateProjectFormRequest, ProjectPageListResponse, \
    UpdateProjectFormRequest
from apps.users.models import UsersModel
from common.user_auth import is_authenticated

router = APIRouter(prefix="/api/projects", tags=['项目模块'])


# =====================================项目相关的接口=================================
@router.post("/", summary="创建项目", status_code=201, response_model=ProjectResponse)
async def create_project(request: CreateProjectFormRequest, user_info: dict = Depends(is_authenticated)):
    """
    创建项目
    :param request: 接口请求
    :param user_info: 用户信息
    :return:
    """
    # 根据用户ID查询用户
    user = await UsersModel.get_or_none(id=request.user)
    if not user:
        raise HTTPException(status_code=422, detail="用户不存在")
    if user.id != user_info["id"]:
        raise HTTPException(status_code=400, detail="用户只能给自己创建项目")
    # 创建项目
    project = await ProjectsModel.create(name=request.name, description=request.description, user=user)
    return project


@router.get("/", summary="获取项目列表", response_model=ProjectPageListResponse)
async def projects_list(user_info: dict = Depends(is_authenticated), page: int = 1, size: int = 10):
    # 根据用户ID查询用户
    user = await UsersModel.get_or_none(id=user_info["id"])
    if not user:
        raise HTTPException(status_code=422, detail="用户不存在")
    # 获取项目列表
    query = ProjectsModel.all().prefetch_related("user")
    # 获取数量总量
    total = await query.count()
    projects = await query.offset((page - 1) * size).limit(size)
    return {"total": total, "data": projects}


@router.get("/{id}", summary="获取项目详情", response_model=ProjectResponse)
async def project_detail(id: int, user_info: dict = Depends(is_authenticated)):
    """
    获取项目详情
    :param id: 项目id
    :param user_info: 用户信息
    :return:
    """
    user = await UsersModel.get_or_none(id=user_info["id"])
    if not user:
        raise HTTPException(status_code=422, detail="用户不存在")
    # 根据项目ID查询项目
    project = await ProjectsModel.get_or_none(id=id).prefetch_related("user")
    if not project:
        raise HTTPException(status_code=422, detail="项目不存在")
    return project


@router.put("/{id}", summary="更新项目", response_model=ProjectResponse)
async def update_project(id: int, request: UpdateProjectFormRequest, user_info: dict = Depends(is_authenticated)):
    """
    更新项目
    :param id: 项目id
    :param request: 修改信息请求
    :param user_info:
    :return:
    """
    user = await UsersModel.get_or_none(id=user_info["id"])
    if not user:
        raise HTTPException(status_code=422, detail="用户不存在")
    if user.id != user_info["id"]:
        raise HTTPException(status_code=400, detail="用户只能修改给自己创建项目")
    # 获取项目详情
    project = await ProjectsModel.get_or_none(id=id).prefetch_related("user")
    if not project:
        raise HTTPException(status_code=422, detail="项目不存在")
    project.name = request.name
    project.description = request.description
    await project.save()
    return project


@router.delete("/{id}", summary="删除项目", status_code=204)
async def update_project(id: int, user_info: dict = Depends(is_authenticated)):
    """
    删除项目
    :param id: 项目id
    :param user_info:
    :return:
    """
    # 获取项目详情
    project = await ProjectsModel.get_or_none(id=id)
    if not project:
        raise HTTPException(status_code=422, detail="项目不存在")
    await project.delete()
