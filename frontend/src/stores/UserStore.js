import { defineStore } from 'pinia'

export const UserStore = defineStore('ustore', {
  // 全局的状态（数据）
  state: () => {
    return {
      // 保存用户token
      token: null,
      // 登录用户名
      username: '',
      // 保存用户信息
      userInfo: null,
      // 表示用户是否登陆过
      isAuthenticated: false,
    }
  },
  // 定义持久化配置
  persist: {
    enabled: true,
    // 用户状态信息持久化配置
    strategies: [
      {
        key: 'userInfo',
        storage: localStorage,
      },
    ],
  },
})
