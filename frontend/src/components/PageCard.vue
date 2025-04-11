<template>
  <el-main>
    <el-card style="border-radius: 10px" body-style="padding: 0 10px;">
      <!--标题-->
      <div class="title">
        <slot name="title"></slot>
      </div>
      <!-- 步骤列表-->
      <div class="main_box">
        <slot name="main"></slot>
      </div>
      <!-- 底部按钮-->
      <div class="bottom_box">
        <slot name="bottom"></slot>
      </div>
    </el-card>
  </el-main>
</template>

<script setup></script>

<style scoped lang="scss">
.el-main {
  margin: 0;
  padding: 5px;

  //标题区域样式
  .title {
    height: 40px;
    display: flex;
    align-items: center;
    margin-left: 5px;
    font: bold 14px/40px '微软雅黑';
    color: var(--el-color-info);
  }

  //主体内容区域样式
  .main_box {
    height: calc(100vh - 270px);
    border-radius: 10px;
    box-shadow: inset 0 0 5px 0 var(--primary-color-line);
    padding: 20px;
    overflow-y: auto;
    z-index: 99;
  }

  //按钮区域样式
  .bottom_box {
    height: 50px;
    display: flex;
    justify-content: flex-start;
    align-items: center;
  }
}
</style>
