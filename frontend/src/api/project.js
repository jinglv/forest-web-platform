import request from '@/api/index'

//=================项目相关接口==============
// 创建项目接口
export function createProject(data) {
  return request({
    url: '/projects/',
    method: 'post',
    data,
  })
}

// 获取项目列表接口
export function projectList(params) {
  return request({
    url: '/projects/',
    method: 'get',
    params,
  })
}

// 编辑项目
export function editProject(id, data) {
  return request({
    url: `/projects/${id}`,
    method: 'put',
    data,
  })
}

// 删除项目
export function deleteProject(id) {
  return request({
    url: `/projects/${id}`,
    method: 'delete',
  })
}
