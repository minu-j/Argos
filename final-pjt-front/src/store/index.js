import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'
import cheerio from 'cheerio'
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
    userId: null,

    ///////////// 박스오피스 //////////////////
    today: {
      year: null,
      month: null,
      date: null
    },
    todayDate: null,
    boxofficeData: [],
    boxOfficeImage: {},

    ///////////// 뉴스 //////////////////
    newsTable: [],
    newsPage: 0
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
      //////////////////////////// 여기서 영화선택 페이지로 넘어가게
      
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
  ////////////////// 박스오피스 /////////////////////
    GET_TODAY(state, payload) {
      console.log()
      state.todayDate = payload
    },
    GET_BOXOFFICE(state, payload) {
      state.boxofficeData = payload
    },
    GET_BOXOFFICE_IMAGE(state, payload) {
      state.boxOfficeImage = payload
    },

  /////////////////////// 뉴스 //////////////////////
    GET_NEWS(state, payload) {
      console.log(payload)
      payload.forEach((news) => {
        state.newsTable.push(news)
      })
      state.newsPage++
    },
    CLEAR_NEWS(state) {
      state.newsTable = []
      state.newsPage = 0
      console.log('잘삭제함', state.newsTable)
    }
  },
  actions: {
    ////////////////// 인증 관련 ///////////////////
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
  ////////////////// 박스오피스 데이터 불러오기 ///////////////////
      
    getBoxoffice(context) {
      const today = new Date()
      let year = today.getFullYear()
      let month = today.getMonth() + 1
      if (String(month).length === 1) {
        let month = '0' + month
      }
      let date = today.getDate() - 1
      if (String(date).length === 1) {
        let date = '0' + date
      }
      const todayDate = String(year) + String(month) + String(date)
      const payload = {
        todayDate,
        year,
        month,
        date
      }
      context.commit('GET_TODAY', payload)

      const KOBIS_API_URL = 'https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'

      axios({
        method: 'GET',
        url: `${KOBIS_API_URL}?key=${process.env.VUE_APP_KOBIS_API_KEY}&targetDt=${context.state.todayDate.todayDate}`
      })
        .then((res) => {
          console.log('박스오피스 로드됨')
          const boxofficeData = res.data.boxOfficeResult.dailyBoxOfficeList
          context.commit('GET_BOXOFFICE', boxofficeData)
          /////////////////// 박스오피스에 맞는 배경이미지 가져오기 //////////////////
          const TMDB_API_URL = 'https://api.themoviedb.org/3/'
          const boxOfficeImage = {}
          context.state.boxofficeData.forEach(element => {
            axios({
              method: 'GET',
              url: TMDB_API_URL + 
                'search/movie?api_key=' + 
                process.env.VUE_APP_TMDB_API_KEY + 
                '&year=' + 
                element.openDt.slice(0, 4) + 
                '&language=ko-KR&page=1&query=' +
                element.movieNm
            })
              .then((res) => {
                boxOfficeImage[element.movieNm] = res.data.results[0].backdrop_path
              })
              .catch((err) => {
                boxOfficeImage[element.movieNm] = false
                console.log(err)
              })   
          });
          context.commit('GET_BOXOFFICE_IMAGE', boxOfficeImage)
        })
        .catch((err) => {
          console.log('박스오피스 로드 실패', err)
          console.log(err)
        })
    },
  
    ////////////////// 뉴스 처음 로드할 때, vuex에 쌓인 뉴스 날리기 //////////////////////
    clearNews(context) {
      context.commit('CLEAR_NEWS')
    },
    ////////////////// 뉴스 데이터 불러오기 //////////////////////
    getNews(context, page) {
      const newsTable = []
      const newsUrl = `/entertainment/movies/${page}`

      // 요청한 페이지가 이미 보고있는 페이지면 로드하지 않기
      if (context.state.newsPage > page && context.state.newsPage === page) {
        console.log('이미 페이지가 로드되었습니다.')
      } else {
        axios.get(newsUrl)
          .then((response) => {
            const $ = cheerio.load(response.data)
            $('.list-type038 > .list > li > .item-box01').map((i, element) => {
              const news = {
                time: null,
                imgSrc: null,
                title: null,
                content: null,
                link: null
              }
              // console.log(element)
              news.time = $(element).find('.txt-time').text()
              news.imgSrc = $(element).find('.img-con > a > img')[0]['attribs']['src']
              news.title = $(element).find('.tit-news').text()
              news.content = $(element).find('.lead').text()
              news.link = $(element).find('.news-con > a')[0]['attribs']['href']
              newsTable.push(news)
            })
            context.commit('GET_NEWS', newsTable)
          })
          .catch((error) => {
            console.log('뉴스 데이터 수신 실패', error)
          })
        }
    },
  },
})



