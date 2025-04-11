import { createRouter, createWebHistory } from 'vue-router'
import { UserStore } from '@/stores/UserStore'
import { ProjectStore } from '@/stores/ProjectStore'
import NProgress from 'nprogress'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/login',
    },
    {
      path: '/login',
      name: 'Login',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/login/LoginView.vue'),
    },
    {
      path: '/register',
      name: 'Register',
      component: () => import('../views/login/RegisterView.vue'),
    },
    {
      path: '/home',
      name: 'Home',
      redirect: '/home/projects',
      component: () => import('../views/home/HomeView.vue'),
      children: [
        {
          path: '/home/projects',
          component: () => import('../views/project/ProjectView.vue'),
          name: 'Project',
          meta: {
            title: '项目管理',
            iconImg: new URL('@/assets/icons/pro_list.svg', import.meta.url).href,
          },
        },
        {
          path: '/home/project/module',
          component: () => import('../views/project/ModuleView.vue'),
          name: 'Module',
          meta: {
            title: '功能模块',
            iconImg: new URL('@/assets/icons/function.svg', import.meta.url).href,
          },
        },
        {
          path: '/home/project/envs',
          component: () => import('../views/project/EnvView.vue'),
          name: 'Env',
          meta: {
            title: '测试环境',
            iconImg: new URL('@/assets/icons/test_env.svg', import.meta.url).href,
          },
        },
        {
          path: '/home/test/cases',
          name: 'Cases',
          component: () => import('../views/manage/TestCaseView.vue'),
          meta: {
            title: '测试用例',
            iconImg: new URL('@/assets/icons/test_case.svg', import.meta.url).href,
          },
        },
        {
          path: '/home/cases/add',
          component: () => import('../views/manage/TestCaseAddView.vue'),
          name: 'addCase',
          meta: {
            title: '新建用例',
            // iconImg: new URL("@/assets/icon2/caseadit.png", import.meta.url).href
          },
        },
        {
          path: '/home/cases/edit/:id',
          component: () => import('../views/manage/TestCaseEditView.vue'),
          name: 'editCase',
          meta: {
            title: '编辑用例',
            // iconImg: new URL("@/assets/icon2/zhihangjilu.png", import.meta.url).href
          },
        },
      ],
    },
  ],
})

// 前置路由导航守卫
router.beforeEach(async (to, from) => {
  // 启动进度条动画
  NProgress.start()

  // 保存历史访问的路由信息保存到全局的pinia中
  const proStore = ProjectStore()
  if (to.meta.title) {
    proStore.addTabs(to)
  }
  if (to.name === 'Register') {
    return
  }
  // 创建用户Store对象
  const userStore = UserStore()
  if (!userStore.token && to.name !== 'Login') {
    return { name: 'Login' }
  }
})

// 后置路由导航守卫
// 在路由变化后完成进度条
router.afterEach(() => {
  NProgress.done()
})

export default router
