import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'
// import { remove } from 'cheerio/lib/api/manipulation'


Vue.use(Vuex)

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
    // getMovie(store, context) {
    //   console.log(`Token ${store.state.token}`)
    //   axios({
    //     method: 'GET',
    //     url: `${API_URL}/api/v1/movie/${context.movie_id}/`,
    //     headers: {
    //       Authorization: `Token ${store.state.token}`
    //     }
    //   })
    //     .then((res) =>{
    //       console.log(res.data)
    //       // // console.log(res.data)
    //       // context.commit('GET_MOVIES', res.data)
    //     })
    //     .catch((err) =>{
    //       console.log(err)
    //     })
    // },
    // ACCOUNTS ACTIONS
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
        })
        .catch(err => console.log(err))
  },
  },
})



