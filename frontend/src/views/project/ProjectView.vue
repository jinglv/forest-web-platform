<template>
  <PageCard>
    <template #title>
      <el-button type="primary" icon="View" @click="addClickBtn">创建项目</el-button>
    </template>
    <template #main>
      <el-table :data="ProList" style="width: calc(100% - 40px)" border>
        <el-table-column prop="name" label="项目名称" />
        <el-table-column prop="description" label="项目说明" />
        <el-table-column prop="user.username" label="创建人" />
        <el-table-column prop="create_time" label="创建时间">
          <template #default="scope">
            {{ dateTools.rTime(scope.row.create_time) }}
          </template>
        </el-table-column>
        <el-table-column label="操作" width="350px">
          <template #default="scope">
            <!--判断是否为当前选中的项目，选中的项目禁用操作-->
            <div v-if="scope.row.id == proStore.projectInfo.id">
              <el-button disabled type="info" icon="Switch">切换项目</el-button>
              <el-button disabled plain type="info" icon="Edit">编辑</el-button>
              <el-button disabled plain type="danger" icon="Delete">删除</el-button>
            </div>
            <div v-else>
              <el-button @click="switchPro(scope.row)" type="primary" icon="Switch"
                >切换项目</el-button
              >
              <el-button @click="clickEdit(scope.row)" plain type="info" icon="Edit"
                >编辑</el-button
              >
              <el-button @click="deletePro(scope.row.id)" plain type="danger" icon="Delete"
                >删除</el-button
              >
            </div>
          </template>
        </el-table-column>
      </el-table>
    </template>
    <template #bottom>
      <el-pagination
        v-model:current-page="pageConfig.page"
        v-model:page-size="pageConfig.size"
        :page-sizes="[10, 20, 30, 400]"
        layout="total, sizes, prev, pager, next, jumper"
        :total="pageConfig.total"
        @current-change="getProjectList"
        @size-change="getProjectList"
      />
    </template>
  </PageCard>
  <!-- 添加项目-->
  <el-dialog v-model="isDlgShow" title="添加项目" width="40%">
    <el-form :model="fromData" label-width="80">
      <el-form-item label="项目名称">
        <el-input @keyup.enter="creatPro" v-model="fromData.name" autocomplete="off" />
      </el-form-item>
      <el-form-item label="项目说明">
        <el-input @keyup.enter="creatPro" v-model="fromData.description" autocomplete="off" />
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="isDlgShow = false">取消</el-button>
        <el-button type="primary" @click="creatPro">确认</el-button>
      </span>
    </template>
  </el-dialog>
  <!-- 修改项目的弹框 -->
  <el-dialog v-model="isEditDlgShow" title="编辑项目" width="40%">
    <el-form :model="fromUpdateData" label-width="80">
      <el-form-item label="项目名称">
        <el-input @keyup.enter="editPro" v-model="fromUpdateData.name" autocomplete="off" />
      </el-form-item>
      <el-form-item label="项目说明">
        <el-input @keyup.enter="creatPro" v-model="fromUpdateData.description" autocomplete="off" />
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="isEditDlgShow = false">取消</el-button>
        <el-button type="primary" @click="editPro">确认</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { ElMessageBox, ElMessage, ElNotification } from 'element-plus'
import dateTools from '@/tools/dateTools'
import PageCard from '@/components/PageCard.vue'
import { projectList, createProject, editProject, deleteProject } from '@/api/project'
import { UserStore } from '@/stores/UserStore'
import { ProjectStore } from '@/stores/ProjectStore'

const ustore = UserStore()
const proStore = ProjectStore()

// ================获取项目列表数据和翻页功能==================
const ProList = ref([])

const pageConfig = reactive({
  page: 1,
  size: 10,
  total: 0,
})

const getProjectList = async () => {
  const res = await projectList()
  ProList.value = res.data.data
  pageConfig.total = res.data.total
}
getProjectList()

// ================创建项目==================
let isDlgShow = ref(false)
let fromData = reactive({
  name: '',
  description: '',
  user: ustore.userInfo.id,
})
// 显示添加窗口
const addClickBtn = () => {
  isDlgShow.value = true
}
// 发送请求添加项目
const creatPro = async () => {
  const response = await createProject(fromData)
  if (response.status === 201) {
    // 弹出提示
    ElNotification({
      title: '项目创建成功',
      type: 'success',
    })
    // 关闭窗口
    isDlgShow.value = false
    // 刷新页面数据
    getProjectList()
  }
}
// ================编辑项目==================
let isEditDlgShow = ref(false)
let fromUpdateData = ref({
  leader: '',
})

// 点击编辑按钮时调用的方法
function clickEdit(pro) {
  isEditDlgShow.value = true
  fromUpdateData.value = { ...pro }
}

// 发送请求修改项目信息
async function editPro() {
  let pro_id = fromUpdateData.value.id
  const response = await editProject(pro_id, fromUpdateData.value)
  if (response.status === 200) {
    ElNotification({
      title: '项目修改成功',
      type: 'success',
    })
    // 关闭窗口
    isEditDlgShow.value = false
    // 刷新页面上的数据
    getProjectList()
  }
}

// ================删除项目==================
const deletePro = (pro_id) => {
  // 调用后端的接口进行删除
  ElMessageBox.confirm('删除操作不可恢复，请确认是否要删除该项目?', '提示', {
    confirmButtonText: '确认',
    cancelButtonText: '取消',
    type: 'warning',
  })
    .then(async () => {
      // 调用后端接口进行删除
      const response = await deleteProject(pro_id)
      if (response.status === 204) {
        ElMessage({
          type: 'success',
          message: '已成功删除该项目',
        })
        // 刷新页面数据
        getProjectList()
      }
    })
    .catch(() => {
      ElMessage({
        type: 'info',
        message: '已取消删除操作',
      })
    })
}

// ================切换项目==================
const switchPro = (pro) => {
  // 清空项目信息
  proStore.$reset()
  // 保存项目信息
  proStore.projectInfo = {
    id: pro.id,
    name: pro.name,
  }
  // 启动菜单
  proStore.isDisabled = false
  // // 获取环境列表
  // proStore.getEnvList()
  // // 获取设备列表
  // proStore.getDeviceList()
  // // 获取模块列表
  // proStore.getModuleList()
  // 提示切换项目
  ElNotification({
    title: '项目切换成功',
    type: 'success',
    message: `当前项目为：${pro.name}`,
    duration: 2000,
    offset: 50,
  })
  // // 跳转到项目功能模块
  // router.push({name: 'moduleList'})
}
</script>

<style lang="scss" scoped>
.el-table,
.el-pagination,
.add-btn {
  margin: 20px;
}
</style>
