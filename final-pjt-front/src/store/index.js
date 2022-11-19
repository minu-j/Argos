import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'
// import { remove } from 'cheerio/lib/api/manipulation'


Vue.use(Vuex)

// const requireAuth = () => (from, to, next) => {
//   const JSONtoken = JSON.parse(localStorage.getItem('vuex'))
//   const token = JSONtoken.token
//   // 로그인 되어있으면 next로 이동
//   if (token) {
//     return next()
//   }else{ // 로그인 안 되어있으면 로그인 페이지로 이동
//   alert('로그인이 필요한 서비스입니다.')
//   next('/login')
//   // 어디로 갈 지 담겨있음
//   // next('from.fullPath')}
//  }
// }

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  // 토큰 관리
  plugins: [
    createPersistedState()
  ],
  state: {
    userLocation: { // 사용자 위치정보
      latitude: null,
      longitude: null,
    },
    // 로그인
    movies: [],
    token: null,
    username: null,
    userId: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_LOCATION(state, payload) { // 위치정보 수집
      state.userLocation.latitude = payload.latitude
      state.userLocation.longitude = payload.longitude
    },

    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    
    // 회원 가입 && 로그인 && 로그아웃을 위한 토큰 저장, 변경
    SAVE_TOKEN(state, token) {
      state.token = token.key
      state.username = token.username
      router.push({ name:'LoginView' })

    },
    SAVE_USER_ID(state, id) {
      state.userId = id
      console.log(id)
      router.push({name: 'HomeView'})
    },
    NULL_TOKEN(state) {
      state.token = null
      router.push({name: 'HomeView'})
    },

  //   DELETE_TOKEN(state){
  //     state.token = remove.state.token
  //     router.push({name: 'HomeView'})
  // },
  },
  actions: {

    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then(res => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch(err => console.log(err))
    },
    logIn(context, payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then(res => {
          context.commit('SAVE_TOKEN', {'key': res.data.key, 'username': username})
          axios({
            method: 'get',
            url: `${API_URL}/accounts/userinfo/${username}/`
          })
            .then(res => {
              context.commit('SAVE_USER_ID', res.data.id)
            })
        })
        .catch(err => console.log(err))
  },
  },
})



