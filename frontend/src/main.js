import { createApp } from 'vue'
import { createPinia } from 'pinia'
// pinia持久化组件
import piniaPluginPersist from 'pinia-plugin-persist'

import App from './App.vue'
import router from './router'

// ------------------elenmentplus导入------------------
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
// ------------------elenmentplus导入end------------------
// 注意修改全局主题颜色后，与element-plus导入的顺序
import './assets/main.css'
// 虚拟进度条
import 'nprogress/nprogress.css'

const app = createApp(App)

// ---------------------elementplus的配置------------------
// 注册elementplus的组件
app.use(ElementPlus, {
  locale: zhCn,
  size: 'small',
})
// 注册elementplus的图标组件
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}
// ---------------------end------------------

//---------------------pinina设置------------------
const uPinia = createPinia()
// 注册持久化插件
uPinia.use(piniaPluginPersist)
app.use(uPinia)

app.use(router)

app.mount('#app')
