import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// ------------------elenmentplus导入------------------
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
// ------------------elenmentplus导入end------------------

const app = createApp(App)

// ---------------------elementplus的配置------------------
// 注册elementplus的组件
app.use(ElementPlus, {
    locale: zhCn,
  })
  // 注册elementplus的图标组件
  for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
  }
// ---------------------end------------------

app.use(createPinia())
app.use(router)

app.mount('#app')
