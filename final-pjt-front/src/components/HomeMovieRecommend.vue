<template>
  <div>
    <div v-if="recommendMovieData.length > 0">
      <div id="recommend-swiper" v-for="(recommendMovies, index) in recommendMovieData" :key="`recommend-${index}`">
        <div>
          <MovieSwiper :recommend-movies="recommendMovies"/>
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
export default {
  components: { MovieSwiper },
  name: 'HomeMovieRecommend',
  data() {
    return {
      recommendMovieData: {}
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
    }
  },
  mounted() {
    const user_id = this.$store.state.userId
    const API_URL = 'http://127.0.0.1:8000'
    const Token = this.$store.state.token
    console.log(`Token ${Token}`)
    axios({
      method: 'GET',
      url: `${API_URL}/accounts/recommend/${user_id}/`,
      headers: {
        Authorization: `Token ${Token}`
      }
    })
      .then((res) =>{
        this.recommendMovieData = res.data.data
        console.log(this.recommendMovieData)
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