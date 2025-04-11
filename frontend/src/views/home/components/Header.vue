<template>
  <div class="header_box">
    <!--左侧按钮，控制菜单折叠-->
    <div class="left_box">
      <el-button
        plain
        size="default"
        v-if="proStore.isCollapse"
        @click="switchCollapse"
        icon="Expand"
      />
      <el-button plain size="default" v-else @click="switchCollapse" icon="Fold" />
    </div>
    <!--中间内容-->
    <div class="center_box">
      <div v-if="proStore.projectInfo.name">{{ proStore.projectInfo.name }}</div>
      <div v-else>项目管理</div>
    </div>
    <!--右侧区域-->
    <div class="right_box">
      <div class="box1">
        <el-button plain size="default" @click="screenFull.toggle()" icon="Rank" />
      </div>
      <div class="box1">
        <el-button plain size="default" icon="Switch">切换项目</el-button>
      </div>
      <div class="box2">
        <el-dropdown trigger="click">
          <el-button plain size="default" icon="User">{{ uStore.username }}</el-button>
          <template #dropdown>
            <el-button plain size="default" @click="logout">退出登录</el-button>
          </template>
        </el-dropdown>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import screenFull from 'screenfull'
import { UserStore } from '@/stores/UserStore'
import { ProjectStore } from '@/stores/ProjectStore'

const router = useRouter()

const uStore = UserStore()
const proStore = ProjectStore()

// 切换菜单折叠
const switchCollapse = () => {
  proStore.isCollapse = !proStore.isCollapse
}

// 退出登录
const logout = () => {
  // 清空pinia中的所有信息
  uStore.$reset()
  proStore.$reset()
  // 跳转到登录页面
  router.push({ name: 'Login' })
}
</script>

<style lang="scss" scoped>
.header_box {
  height: 55px;
  display: flex;
  justify-content: space-between;
  align-items: center;

  .left_box {
    margin-left: 10px;
  }
  //调整项目名称样式
  .center_box {
    font: bold 16px/36px '微软雅黑';
    color: var(--el-color-info);
    border: 1px dashed var(--el-color-primary);
    padding: 0 30px;
    border-radius: 15px;
  }

  .right_box {
    display: flex;
    justify-content: space-between;
    align-items: center;
    .box1 {
      margin-right: 10px;
    }
    .box2 {
      margin-right: 40px;
      cursor: pointer;
    }
  }
}
</style>
