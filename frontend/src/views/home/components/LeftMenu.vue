<template>
  <!--顶部logo图表-->
  <div class="logo">
    <img src="@/assets/logo.svg" alt="logo" />
    <div class="title" v-if="!proStore.isCollapse">Web自动化测试平台</div>
  </div>
  <!--菜单-->
  <el-menu
    :default-active="$route.path"
    router
    :collapse="proStore.isCollapse"
    collapse-transition
    size="large"
  >
    <!-- 嵌套的菜单-->
    <template v-for="item in MenuList" :key="item.path">
      <el-sub-menu
        v-if="item.children && item.children.length"
        :index="item.name"
        :disabled="proStore.isDisabled"
      >
        <template #title>
          <el-icon>
            <img :src="item.iconImg" width="20" alt="" />
          </el-icon>
          <span>{{ item.name }}</span>
        </template>
        <el-menu-item
          class="child-menu"
          :index="child.path"
          v-for="child in item.children"
          :key="child.path"
        >
          <template #title>
            <el-icon>
              <img :src="child.iconImg" width="20" alt="" />
            </el-icon>
            <span>{{ child.name }}</span>
          </template>
        </el-menu-item>
      </el-sub-menu>
      <el-menu-item class="menu" v-else :index="item.path">
        <el-icon>
          <img :src="item.iconImg" width="20" alt="" />
        </el-icon>
        <template #title>
          <span>{{ item.name }}</span>
        </template>
      </el-menu-item>
    </template>
  </el-menu>
</template>

<script setup>
import { ProjectStore } from '@/stores/ProjectStore'
import { MenuList } from '@/data/LeftMenu'

const proStore = ProjectStore()
</script>

<style lang="scss" scoped>
.logo {
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  //logo图标样式
  img {
    height: 40px;
    width: 40px;
  }

  //标题样式
  .title {
    margin-left: 5px;
    font-size: 16px;
    font-weight: bold;
    color: var(--el-color-primary);
    overflow: hidden; /* 内容溢出隐藏 */
    white-space: nowrap; /* 禁止自动换行 */
  }
}
// 修改菜单样式
.el-menu {
  border-right: none;
  height: calc(100vh - 60px);
  overflow: auto;

  :deep(.el-menu-item),
  :deep(.el-sub-menu__title) {
    .el-icon {
      width: 24px;
      height: 24px;
      display: flex;
      align-items: center;
      justify-content: center;

      img {
        width: 20px;
        height: 20px;
      }
    }
  }
}
.menu {
  border-radius: 10px;
  border: 1px dashed #fff;
  // 阴影（内阴影）
  box-shadow: inset 0 0 2px var(--primary-color-line);
  //鼠标悬浮时样式
  &:hover {
    background: none;
    color: var(--el-color-primary);
    box-shadow: inset 0 0 3px var(--el-color-primary);
  }

  //菜单激活时的样式
  &.is-active {
    color: var(--el-color-primary);
    border: 1px dashed var(--el-color-primary);
  }
}

//自定义菜单的样式
.child-menu {
  border-radius: 10px;
  width: 180px;
  height: 40px;
  margin: 4px auto;
  border: 1px dashed #fff;
  // 阴影（内阴影）
  box-shadow: inset 0 0 2px var(--primary-color-line);
  //鼠标悬浮时样式
  &:hover {
    background: none;
    color: var(--el-color-primary);
    box-shadow: inset 0 0 3px var(--el-color-primary);
  }

  //菜单激活时的样式
  &.is-active {
    height: 40px;
    color: var(--el-color-primary);
    border: 1px dashed var(--el-color-primary);
  }
}

// 收起时的样式
.el-menu--collapse {
  :deep(.el-menu-item),
  :deep(.el-sub-menu__title) {
    .el-icon {
      margin: 0 !important;
      width: 100% !important;
      text-align: center;
    }
  }
}

// 修改菜单项激活样式
:deep(.el-menu-item.is-active) {
  background-color: transparent;
  color: var(--el-color-primary);
  border: 1px dashed var(--el-color-primary);
}
</style>
