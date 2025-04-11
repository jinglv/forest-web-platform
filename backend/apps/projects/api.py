# @Time：2025/3/26 09:57
# @Author：jinglv

from fastapi import APIRouter, HTTPException, Depends

from apps.projects.models import ProjectsModel, EnvsModel, ProjectModuleModel
from apps.projects.schemas import ProjectResponse, CreateProjectFormRequest, ProjectPageListResponse, \
    UpdateProjectFormRequest, CreateEnvFormRequest, EnvResponse, UpdateEnvFormRequest, ProjectModulResponse, \
    CreateProjectModuleFormRequest, UpdateProjectModuleFormRequest
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
async def delete_project(id: int, user_info: dict = Depends(is_authenticated)):
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


# =====================================项目测试环境相关的接口=================================
@router.post("/env", summary="创建项目测试环境", status_code=201, response_model=EnvResponse)
async def create_env(request: CreateEnvFormRequest, user_info: dict = Depends(is_authenticated)):
    """
    创建项目测试环境
    :param request: 接口请求
    :param user_info: 用户信息
    :return:
    """
    # 根据用户ID查询用户
    user = await UsersModel.get_or_none(id=user_info["id"])
    if not user:
        raise HTTPException(status_code=422, detail="用户不存在")
    if user.id != user_info["id"]:
        raise HTTPException(status_code=400, detail="用户只能给自己创建项目测试环境")
    project = await ProjectsModel.get_or_none(id=request.project_id)
    if not project:
        raise HTTPException(status_code=422, detail="传入的项目ID不存在")
    # 创建项目测试环境
    env = await EnvsModel.create(**request.model_dump())
    return env


@router.get('/env/list', summary='获取项目测试环境列表', response_model=list[EnvResponse])
async def env_list(project_id: int | None = None, user_info: dict = Depends(is_authenticated)):
    """
    项目测试环境列表
    :param project_id:
    :param user_info:
    :return:
    """
    query = EnvsModel.all()
    if project_id:
        project = await ProjectsModel.get_or_none(id=project_id)
        query = query.filter(project=project)
    envs = await query
    return envs


@router.get('/env/{id}', summary='获取单个项目测试环境详情', response_model=EnvResponse)
async def get_env(id: int, user_info: dict = Depends(is_authenticated)):
    """
    获取项目测试环境详情
    :param id:
    :param user_info:
    :return:
    """
    env = await EnvsModel.get_or_none(id=id)
    if not env:
        raise HTTPException(status_code=422, detail="环境不存在")
    return env


@router.put('/env/{id}', summary='更新项目测试环境', response_model=EnvResponse)
async def update_env(id: int, item: UpdateEnvFormRequest, user_info: dict = Depends(is_authenticated)):
    """
    更新项目测试环境
    :param id:
    :param item:
    :param user_info:
    :return:
    """
    env = await EnvsModel.get_or_none(id=id)
    if not env:
        raise HTTPException(status_code=422, detail="环境不存在")
    env = await env.update_from_dict(item.model_dump(exclude_unset=True))
    await env.save()
    return env


@router.delete('/env/{id}', summary='删除项目测试环境', status_code=204)
async def delete_env(id: int, user_info: dict = Depends(is_authenticated)):
    """
    删除项目测试环境
    :param id:
    :param user_info:
    :return:
    """
    env = await EnvsModel.get_or_none(id=id)
    if not env:
        raise HTTPException(status_code=422, detail="环境不存在")
    await env.delete()


# =====================================项目模块相关的接口=================================
@router.post('/module', summary='创建项目模块', status_code=201, response_model=ProjectModulResponse)
async def create_module(request: CreateProjectModuleFormRequest, user_info: dict = Depends(is_authenticated), ):
    """
    创建项目模块
    :param request:
    :param user_info:
    :return:
    """
    project = await ProjectsModel.get_or_none(id=request.project_id)
    if not project:
        raise HTTPException(status_code=422, detail="传入的项目ID不存在")
    module = await ProjectModuleModel.create(name=request.name, project=project)
    return module


@router.put('/module/{id}', summary='更新项目模块', status_code=201, response_model=ProjectModulResponse)
async def update_module(id: int, request: UpdateProjectModuleFormRequest,
                        user_info: dict = Depends(is_authenticated), ):
    """
    更新项目模块
    :param id:
    :param request:
    :param user_info:
    :return:
    """
    module = await ProjectModuleModel.get_or_none(id=id)
    if not module:
        raise HTTPException(status_code=422, detail="模块不存在")
    module.name = request.name
    await module.save()
    return module


@router.delete('/module/{id}', summary='删除项目模块', status_code=204)
async def delete_module(id: int, user_info: dict = Depends(is_authenticated)):
    """
    删除项目模块
    :param id:
    :param user_info:
    :return:
    """
    module = await ProjectModuleModel.get_or_none(id=id)
    if not module:
        raise HTTPException(status_code=422, detail="模块不存在")
    await module.delete()


@router.get('/module/list', summary='获取项目模块列表', response_model=list[ProjectModulResponse])
async def get_modules(project: int | None = None, user_info: dict = Depends(is_authenticated)):
    """
    获取项目模块列表
    :param project:
    :param user_info:
    :return:
    """
    query = ProjectModuleModel.all()
    if project:
        project = await ProjectsModel.get_or_none(id=project)
        query = query.filter(project=project)
    modules = await query
    return modules


@router.get('/module/{id}', summary='获取单个项目模块详情', response_model=ProjectModulResponse)
async def get_module(id: int, user_info: dict = Depends(is_authenticated)):
    """
    获取单个项目模块详情
    :param id:
    :param user_info:
    :return:
    """
    module = await ProjectModuleModel.get_or_none(id=id)
    if not module:
        raise HTTPException(status_code=422, detail="环境不存在")
    return module
