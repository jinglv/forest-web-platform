<template>
  <div class="main">
    <div class="register_box">
      <div class="header">
        <img src="@/assets/logo.svg" alt="logo" class="logo" />
        <div class="title">小森林Web测试平台</div>
      </div>
      <div class="register-form">
        <el-form :model="registerFrom" :rules="registerRules" ref="registerFormRef">
          <el-form-item prop="username">
            <el-input
              prefix-icon="UserFilled"
              size="large"
              v-model="registerFrom.username"
              autocomplete="off"
              placeholder="请输入用户名"
            />
          </el-form-item>
          <el-form-item prop="password">
            <el-input
              prefix-icon="Unlock"
              size="large"
              type="password"
              v-model="registerFrom.password"
              autocomplete="off"
              placeholder="请输入密码"
            />
          </el-form-item>
          <el-form-item prop="password_confirm">
            <el-input
              prefix-icon="Lock"
              size="large"
              type="password"
              v-model="registerFrom.password_confirm"
              autocomplete="off"
              placeholder="再次确认密码"
            />
          </el-form-item>
          <el-form-item prop="nickname">
            <el-input
              prefix-icon="Avatar"
              size="large"
              v-model="registerFrom.nickname"
              autocomplete="off"
              placeholder="请输入名字 "
            />
          </el-form-item>
          <el-form-item prop="mobile">
            <el-input
              prefix-icon="Phone"
              size="large"
              v-model="registerFrom.mobile"
              autocomplete="off"
              placeholder="请输入电话"
            />
          </el-form-item>
          <el-form-item prop="email">
            <el-input
              prefix-icon="Message"
              size="large"
              v-model="registerFrom.email"
              autocomplete="off"
              placeholder="请输入邮箱"
            />
          </el-form-item>

          <el-form-item>
            <el-button
              size="large"
              type="warning"
              @click="registerSubmit(registerFormRef)"
              icon="CircleCheck"
              style="width: 100%"
              >点击注册
            </el-button>
          </el-form-item>
          <!-- 没有账号，点击注册-->
          <el-link type="warning" @click="$router.push('/Login')">已有账号，点击登录</el-link>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ElMessage, ElNotification } from 'element-plus'
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { register } from '@/api/users'

// 创建路由对象
const router = useRouter()

// 登录的表单数据
const registerFrom = reactive({
  username: '',
  password: '',
  password_confirm: '',
  email: '',
  mobile: '',
  nickname: '',
})

// 校验账号密码
const registerRules = reactive({
  username: [
    { required: true, message: '账号不能为空', trigger: 'blur' },
    { min: 4, max: 16, message: '账号必须在4-16位之间', trigger: 'blur' },
  ],
  password: [
    { required: true, message: '密码不能为空', trigger: 'blur' },
    { min: 6, max: 16, message: '密码必须在6-16位之间', trigger: 'blur' },
  ],
  password_confirm: [
    { required: true, message: '密码不能为空', trigger: 'blur' },
    { min: 6, max: 16, message: '密码必须在6-16位之间', trigger: 'blur' },
  ],
  nickname: [{ required: true, message: '名字不能为空', trigger: 'blur' }],
  mobile: [{ required: true, message: '电话不能为空', trigger: 'blur' }],
  email: [{ required: true, message: '邮箱不能为空', trigger: 'blur' }],
})

// 表单引用对象
const registerFormRef = ref()

// 定义注册的方法
const registerSubmit = async (formEl) => {
  // 先对表单进行预校验，校验不通过则不会发请求
  if (!formEl) return
  await formEl.validate(async (valid) => {
    // 参数校验通过
    if (valid) {
      const response = await register(registerFrom)
      if (response.status == 200) {
        ElNotification({
          title: 'Success',
          message: '用户注册成功',
          type: 'success',
          duration: 2000,
        })
        // 用户注册成功，跳转到登录页面
        router.push({ name: 'Login' })
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
</script>

<style lang="scss" scoped>
.main {
  width: 100vw;
  height: 100vh;
  background-image: url('@/assets/register-bg.svg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: fixed;
  .register_box {
    width: 600px;
    height: 660px;
    position: absolute;
    top: calc(50vh - 330px);
    left: calc(50vw - 280px);
    background: rgba(255, 255, 255, 0.7);
    border-radius: 20px;
    box-shadow: 0 0 5px var(--el-color-warning);
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
        color: var(--el-color-warning);
        margin-left: 10px;
      }
    }
    .register-form {
      padding: 0 30px;

      .el-form-item {
        margin-bottom: 20px;
      }
    }
  }
}
</style>
