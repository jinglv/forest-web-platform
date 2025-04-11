import { ref } from 'vue'

// 使用 Intl.DateTimeFormat 进行日期格式化
const dateFormatter = new Intl.DateTimeFormat('zh-CN', {
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
  hour: '2-digit',
  minute: '2-digit',
  second: '2-digit',
  hour12: false,
})

const dateOnlyFormatter = new Intl.DateTimeFormat('zh-CN', {
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
})

export const useTime = () => {
  const year = ref(0)
  const month = ref(0)
  const week = ref('')
  const day = ref(0)
  const hour = ref('00')
  const minute = ref('00')
  const second = ref('00')
  const nowTime = ref('')

  const updateTime = () => {
    const date = new Date()
    year.value = date.getFullYear()
    month.value = date.getMonth() + 1
    week.value = new Intl.DateTimeFormat('zh-CN', { weekday: 'narrow' }).format(date)
    day.value = date.getDate()

    // 使用 padStart 统一处理补零
    hour.value = date.getHours().toString().padStart(2, '0')
    minute.value = date.getMinutes().toString().padStart(2, '0')
    second.value = date.getSeconds().toString().padStart(2, '0')

    nowTime.value = `${year.value}年${month.value}月${day.value}日 ${hour.value}:${minute.value}:${second.value}`
  }

  updateTime()

  return { year, month, day, hour, minute, second, week, nowTime }
}

export default {
  // 格式化日期时间
  rTime(date) {
    return dateFormatter.format(new Date(date)).replace(/\//g, '-')
  },

  // 格式化日期
  rDate(date) {
    return dateOnlyFormatter.format(new Date(date)).replace(/\//g, '-')
  },
}
