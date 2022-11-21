<template>
  <div>
    <div id="recommend-swiper" v-for="(recommendMovies, index) in recommendMovieData" :key="`recommend-${index}`">
      <div>
        <MovieSwiper :recommend-movies="recommendMovies"/>
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