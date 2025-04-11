<template>
  <el-container>
    <!-- 左侧侧边栏 -->
    <el-aside :style="{ width: proStore.isCollapse ? '65px' : '200px', height: '100vh' }">
      <LeftMenu />
    </el-aside>
    <el-container>
      <!-- 页面头部内容 -->
      <el-header>
        <Header />
      </el-header>
      <!-- 页面主体内容 -->
      <el-main>
        <!-- 标签栏 -->
        <Tabs />
        <!-- 主体内容区域 -->
        <div class="main_box">
          <router-view></router-view>
        </div>
      </el-main>
      <!-- 页面底部内容 -->
      <el-footer>
        <Footer />
      </el-footer>
    </el-container>
  </el-container>
</template>

<script setup>
import Header from './components/Header.vue'
import LeftMenu from './components/LeftMenu.vue'
import Tabs from './components/Tabs.vue'
import Footer from './components/Footer.vue'

import { ProjectStore } from '@/stores/ProjectStore'

const proStore = ProjectStore()
</script>

<style lang="scss" scoped>
//页面整体布局样式
.el-container {
  .el-aside {
    //左侧菜单右边边框阴影
    box-shadow: 5px 0 5px -3px rgba(0, 0, 0, 0.1);
    transition: width 0.3s ease-in-out; /* 定义宽度变化的过渡效果 */
  }

  .el-header {
    //头部顶部阴影
    box-shadow: 0 5px 5px -3px rgba(0, 0, 0, 0.1);
    padding: 0;
    height: 55px;
    z-index: 99;
  }

  .el-footer {
    height: 30px;
    //页脚顶部阴影
    box-shadow: 0 -5px 5px -3px rgba(0, 0, 0, 0.1);
    z-index: 99;
  }

  .el-main {
    padding: 2px;
    overflow-y: auto;
  }

  .main_box {
    height: calc(100vh - 130px);
    overflow-y: hidden;
  }
}
</style>
