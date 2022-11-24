<template>
  <div>
    <div v-if="recommendMovieData.length > 0">
      <div id="recommend-swiper" v-for="(recommendMovies, index) in recommendMovieData" :key="`recommend-${index}`">
        <div>
          <MovieSwiper :recommend-movies="recommendMovies"/>
        </div>
      </div>
      <div>
        <div id="get-next-row">
          <movie-swiper-loader id="recommend-swiper"/>
        </div>
      </div>
    </div>
    <div v-else >
      <div v-if="isLogin" id="offer-rating">
        취향에 맞는 추천 영화를 찾아보세요
        <div @click="goRating" id="offer-rating-link">본 영화 평가하러 가기 →</div>
      </div>
      <div v-else id="offer-login">
        로그인하여 취향에 맞는 추천 영화를 찾아보세요
        <div @click="goLogin" id="offer-login-link">로그인 하러 가기 →</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import MovieSwiper from './MovieSwiper.vue'
import MovieSwiperLoader from './MovieSwiperLoader.vue'
export default {
  components: { MovieSwiper, MovieSwiperLoader },
  name: 'HomeMovieRecommend',
  data() {
    return {
      recommendMovieData: []
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    goLogin() {
      this.$router.push({ name:'LoginView' })
    },
    goRating() {
      this.$router.push({ name:'MovieRating' })
    },
    setObserver() {
      // 로더 띄우기 용 감시 옵저버
      const target = document.querySelector('#get-next-row').firstChild

      const showLastMovie = (entries) => {

        // Destructuring
        const [{isIntersecting}] = entries;
        
        if (isIntersecting) {
          this.getMovieData()
        }
      };

      // intersection observer 생성자 초기화 (관찰자)
      const io = new IntersectionObserver(showLastMovie, {
        root: null,
        threshold: 0.5,
      })

      // NodeList의 각 요소들 감시 시작
      io.observe(target);
    },
    getMovieData() {
      const user_id = this.$store.state.userId
      const API_URL = this.$store.state.API_URL
      const Token = this.$store.state.token
      axios({
        method: 'GET',
        url: `${API_URL}/accounts/recommend/${user_id}/`,
        headers: {
          Authorization: `Token ${Token}`
        }
      })
        .then((res) =>{
          res.data.data.forEach(element => {
            this.recommendMovieData.push(element)
          });
        })
        .catch((err) =>{
          console.log(err)
        })
    }
  },
  mounted() {
    const user_id = this.$store.state.userId
    const API_URL = this.$store.state.API_URL
    const Token = this.$store.state.token
    axios({
      method: 'GET',
      url: `${API_URL}/accounts/recommend/${user_id}/`,
      headers: {
        Authorization: `Token ${Token}`
      }
    })
      .then((res) =>{
        this.recommendMovieData = res.data.data
        console.log(res.data.data)
      })

      // 영화 로딩 후 옵저버 설정
      .then(() => {
        this.setObserver()
      })
      .catch((err) =>{
        console.log(err)
      })
  }
}
</script>

<style lang="scss" scoped>
  @import './HomeMovieRecommend.scss';
</style>