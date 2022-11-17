import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'
import axios from 'axios'

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
  },
  getters: {
    isLogin(state){
      return state.token ? true : false
    },
    loggedIn(state){
      return !!state.user
    },
  },
  mutations: {
    GET_LOCATION(state, payload) { // 위치정보 수집
      state.userLocation.latitude = payload.latitude
      state.userLocation.longitude = payload.longitude
    },

    // 회원 가임 && 로그인 && 로그아웃
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'HomeView'})
    },
    NULL_TOKEN(state) {
      state.token = null
      router.push({ name: 'HomeView' })
    }


  },
  actions: {
    // ---------
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
        headers: {
          Authorizations: `Token ${context.state.token}`
        }
      })
        .then((res) =>{
          // console.log(res, context)
          // console.log(res.data)
          context.commit('GET_MOVIES', res.data)
        })
        .catch((err) =>{
          console.log(err)
        })
    },
    // 회원가입
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    //로그인
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) =>{
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // 로그 아웃
    logOut() {
      this.$store.commit('NULL_TOKEN', )
    }
  },
  modules: {
  }
})


