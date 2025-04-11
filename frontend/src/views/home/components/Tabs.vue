<template>
  <div class="tabs_box">
    <el-tabs icon="UserFilled" v-model="$route.path" @tab-click="clickTab" @tab-remove="clickDel">
      <!--根据历史访问的路由信息去渲染标签， 非当前访问的路由页面，则显示关闭按钮-->
      <div v-for="i in proStore.tabs">
        <el-tab-pane v-if="$route.path !== i.path" :name="i.path" closable>
          <template #label>
            <img :src="i.iconImg" width="20" alt="" style="margin-right: 10px" />
            <span>{{ i.name }}</span>
          </template>
        </el-tab-pane>
        <el-tab-pane v-else :name="i.path">
          <template #label>
            <img :src="i.iconImg" width="20" alt="" style="margin-right: 10px" />
            <span>{{ i.name }}</span>
          </template>
        </el-tab-pane>
      </div>
    </el-tabs>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ProjectStore } from '@/stores/ProjectStore'

const router = useRouter() // 添加 route
const proStore = ProjectStore()

// 点击选项卡
function clickTab(ele) {
  router.push(ele.props.name)
}

// 点击删除的方法
function clickDel(item) {
  proStore.deleteTabs(item)
}
</script>

<style lang="scss" scoped>
.tabs_box {
  height: 40px;
  box-shadow: 0 3px 5px -3px rgba(0, 0, 0, 0.1);
  z-index: 99;
  padding: 0 10px;

  .el-tabs--border-card {
    border: none;
  }
}
</style>
