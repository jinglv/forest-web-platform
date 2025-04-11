export const MenuList = [
  {
    name: '项目管理',
    path: '/home/projects',
    iconImg: new URL('@/assets/icons/pro_list.svg', import.meta.url).href,
  },
  {
    name: '项目详情',
    iconImg: new URL('@/assets/icons/pro_detail.svg', import.meta.url).href,
    children: [
      {
        name: '功能模块',
        path: '/home/project/module',
        iconImg: new URL('@/assets/icons/function.svg', import.meta.url).href,
      },
      {
        name: '测试环境',
        path: '/home/project/envs',
        iconImg: new URL('@/assets/icons/test_env.svg', import.meta.url).href,
      },
    ],
  },
  {
    name: '测试管理',
    iconImg: new URL('@/assets/icons/test_manage.svg', import.meta.url).href,
    children: [
      {
        name: '测试用例',
        path: '/home/test/cases',
        iconImg: new URL('@/assets/icons/test_case.svg', import.meta.url).href,
      },
      {
        name: '测试套件',
        path: '/home/test/suites',
        iconImg: new URL('@/assets/icons/test_suite.svg', import.meta.url).href,
      },
    ],
  },
  {
    name: '测试计划',
    iconImg: new URL('@/assets/icons/test_plan.svg', import.meta.url).href,
    children: [
      {
        name: '任务列表',
        path: '/home/plan/task',
        iconImg: new URL('@/assets/icons/plan_task.svg', import.meta.url).href,
      },
      {
        name: '定时任务',
        path: '/home/plan/cronjob',
        iconImg: new URL('@/assets/icons/cronjob.svg', import.meta.url).href,
      },
    ],
  },
  {
    name: '测试报表',
    iconImg: new URL('@/assets/icons/test_report.svg', import.meta.url).href,
    children: [
      {
        name: '执行记录',
        path: '/home/records',
        iconImg: new URL('@/assets/icons/records.svg', import.meta.url).href,
      },
    ],
  },
  {
    name: '分布式设备',
    iconImg: new URL('@/assets/icons/shebei.svg', import.meta.url).href,
    children: [
      {
        name: '设备列表',
        path: '/home/device',
        iconImg: new URL('@/assets/icons/device.svg', import.meta.url).href,
      },
    ],
  },
]
