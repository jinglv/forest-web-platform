import { defineStore } from 'pinia'

export const ProjectStore = defineStore('proStore', {
  // 全局的状态（数据）
  state: () => {
    return {
      // 左边菜单是否折叠
      isCollapse: false,
      // 保存历史访问的路由记录
      tabs: [],
      // 当前选中的项目
      projectInfo: {},
      //是否禁用菜单
      isDisabled: true,
    }
  },
  actions: {
    // 保存路由信息到tabs中的方法
    addTabs(route) {
      // 查找该路由地方已经保存
      const res = this.tabs.find((item) => {
        return route.path === item.path
      })
      // 如果没有保存，则进行保存
      if (!res) {
        this.tabs.push({
          name: route.meta.title,
          path: route.path,
          icon: route.meta.icon,
          iconImg: route.meta.iconImg,
        })
      }
    },
    // 删除tabs中的路由信息
    deleteTabs(path) {
      this.tabs = this.tabs.filter((item) => {
        return item.path !== path
      })
    },
  },
  // 定义持久化配置
  persist: {
    enabled: true,
    // 用户状态信息持久化配置
    strategies: [
      {
        key: 'projectStore',
        storage: localStorage,
      },
    ],
  },
})
