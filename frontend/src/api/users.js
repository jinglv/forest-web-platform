import request from '@/api/index'

// 注册接口
export function register(data) {
    return request({
        url: 'users/register',
        method: 'post',
        data,
    })
}

// 登录接口
export function login(data) {
  return request({
    url: 'users/login',
    method: 'post',
    data,
  })
}

// 校验token接口
export function verify(data) {
  return request({
    url: 'users/verify',
    method: 'post',
    data,
  })
}