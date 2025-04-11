<template>
  <div class="main">
    <div class="login_box">
      <div class="header">
        <img src="@/assets/logo.svg" alt="logo" class="logo" />
        <div class="title">小森林Web测试平台</div>
      </div>
      <div class="login-form">
        <el-form :model="loginFrom" :rules="loginRules" ref="loginFormRef">
          <el-form-item prop="username">
            <el-input
              prefix-icon="UserFilled"
              size="default"
              v-model="loginFrom.username"
              autocomplete="off"
              placeholder="请输入邮箱|电话|用户名 "
            />
          </el-form-item>
          <el-form-item prop="password">
            <el-input
              prefix-icon="Lock"
              size="default"
              type="password"
              v-model="loginFrom.password"
              autocomplete="off"
              placeholder="请输入密码"
            />
          </el-form-item>
          <el-form-item>
            <el-switch v-model="loginFrom.status" inactive-text="记住登录状态" />
          </el-form-item>
          <el-form-item>
            <el-button
              size="default"
              type="primary"
              @click="loginSubmit(loginFormRef)"
              icon="CircleCheck"
              style="width: 100%"
              >点击登录
            </el-button>
          </el-form-item>
          <!-- 没有账号，点击注册-->
          <el-link type="primary" @click="$router.push('/Register')" style="margin-top: -20px"
            >没有账号，点击注册</el-link
          >
        </el-form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ElMessage, ElNotification } from 'element-plus'
import { ref, reactive, onBeforeMount } from 'vue'
import { useRouter } from 'vue-router'
import { login } from '@/api/users'
import { UserStore } from '@/stores/UserStore'

// 创建路由对象
const router = useRouter()
// 创建用户Store对象
const userStore = UserStore()

// 定义登录的表单数据
const loginFrom = reactive({
  username: 'admin',
  password: '123456',
  status: true,
})

// 定义表单的验证对象和规则
const loginFormRef = ref()
const loginRules = {
  username: [
    { required: true, message: '账号不能为空', trigger: 'blur' },
    { min: 4, max: 16, message: '账号必须在4-16位之间', trigger: 'blur' },
  ],
  password: [
    { required: true, message: '密码不能为空', trigger: 'blur' },
    { min: 6, max: 16, message: '密码必须在6-16位之间', trigger: 'blur' },
  ],
}
// 定义登录的方法
const loginSubmit = async (formEl) => {
  // 先对表单进行预校验，校验不通过则不会发请求
  if (!formEl) return
  await formEl.validate(async (valid) => {
    // 参数校验通过
    if (valid) {
      const response = await login(loginFrom)
      if (response.status == 200) {
        ElNotification({
          title: 'Success',
          message: '身份校验通过,登录成功',
          type: 'success',
          duration: 2000,
        })
        // 保存用户登录之后的token用户信息
        userStore.token = response.data.token
        userStore.username = loginFrom.username
        userStore.userInfo = response.data.user
        //修改认证的状态
        if (loginFrom.status) {
          userStore.isAuthenticated = true
        }
        // 登录成功，跳转到项目页面
        router.push({ name: 'Home' })
      } else {
        ElMessage({
          type: 'error',
          message: response.data.msg,
          duration: 2000,
        })
      }
    }
  })
}

// 如果登录过由用户信息，直接调跳转到首页
onBeforeMount(() => {
  if (userStore.isAuthenticated && userStore.token) {
    ElMessage({
      type: 'info',
      message: '您已经登过，2秒之后为您跳转到到首页',
    })
  }
  setTimeout(() => {
    router.push({ name: 'Home' })
  }, 2000)
})
</script>

<style lang="scss" scoped>
.main {
  width: 100vw;
  height: 100vh;
  background-image: url('@/assets/login-bg.svg');
  background-size: 100% auto;
  background-position: center;
  background-repeat: no-repeat;
  position: fixed;
  .login_box {
    width: 400px;
    height: 360px;
    box-shadow: 0 0 5px var(--el-color-primary);
    position: absolute;
    top: calc(50vh - 230px);
    left: calc(50vw - 250px);
    border-radius: 20px;
    padding: 20px;
    background: rgba(255, 255, 255, 0.8);
  }
  .header {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 150px;
    .logo {
      width: 100px;
      height: 100px;
    }
    .title {
      font-size: 30px;
      font-weight: bold;
      color: var(--el-color-primary);
      margin-left: 10px;
    }
  }
  .login-form {
    padding: 0 30px;
    .el-form-item {
      margin-bottom: 20px;
    }
  }
}
</style>
