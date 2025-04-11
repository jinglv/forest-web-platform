import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    // vueDevTools(),
  ],
  server: {
    host: '0.0.0.0',
    port: 8088,
    hmr: true,
    // 运行之后，自动打开浏览器
    open: true,
    proxy: {
      '/api': {
        // 接口地址
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        ws: true,
        // 重写路径，注意后台接口地址统一前缀
        rewrite: (path) => path.replace(/^\/api/, '/api'),
      },
    },
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
})