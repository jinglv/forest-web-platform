import axios from 'axios'
import { ElMessage } from 'element-plus'
import { UserStore } from '@/stores/UserStore'

// 创建一个axios请求对象
const service = axios.create({
  // 配置根请求地址 baseURL: process.env.VUE_APP_BASE_API
  baseURL: '/api',
  // 用户配置请求接口跨域时是否需要凭证
  withCredentials: false,
  // withCredentials: true, // send cookies when cross-domain requests
  timeout: 5000, // request timeout
  // 全局请求头
  headers: {
    'Content-Type': 'application/json;charset=UTF-8',
  },
  // 设置请求成功状态码范围
  validateStatus: function (status) {
    return true
  },
  // 运行发送跨域请求
  crossDomain: true,
})

// 设置请求拦截器
service.interceptors.request.use(
  (config) => {
    console.info(config)
    // 判断当前的请求的接口是否需要权限校验，本地是否存在token，如果需要则添加token
    if (
      config.url === 'users/login' ||
      config.url === 'users/register' ||
      config.url === 'users/verify' ||
      config.url === 'users/refresh'
    ) {
      return config
    }

    const ustore = UserStore()
    // 如果不是登录和注册判断是否有token
    if (ustore.token) {
      config.headers['Authorization'] = 'Bearer ' + ustore.token
    } else {
      // 全局数据
      ustore.$reset()
      // 重定向到首页
      window.location.href = '/'
    }
    return config
  },
  (error) => {
    // 对请求错误做些什么
    return Promise.reject(error)
  },
)

// 设置响应拦截器
service.interceptors.response.use(
  (response) => {
    if (response.status === 200) return response
    if (response.status === 201) return response
    if (response.status === 204) return response
    // 异常响应状态码的处理
    // 判断响应状态码是否为401,并且不是登录接口
    // 其他的响应状态码提示
    ElMessage({
      message: response.data.msg,
      type: 'warning',
      duration: 3000,
    })
    return response
  },
  (error) => {
    // 对响应错误做点什么
    return Promise.reject(error)
  },
)

// 导出请求方法
export default service
