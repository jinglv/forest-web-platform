# frontend

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```

## 项目安装依赖
```sh
# 先安装element-plus，
pnpm install element-plus

# 再安装@element-plus/icons-vue
pnpm install @element-plus/icons-vue

# 安装axios
pnpm install  axios
```

## element-plus的环境配置
在main.js中
```js
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

```

## 图标图片资源下载地址
- 阿里巴巴图标库：https://www.iconfont.cn
- 字节图标库：https://iconpark.oceanengine.com/official