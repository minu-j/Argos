<template>
  <div id="movie-detail-page">
    <div id="movie-detail">
      <movie-detail-header :movie-data="movieData"/>
      <!-- 스트리밍 서비스 이용 가능시 렌더 -->
      <div v-if="movieData.providers.length > 0">
        <div class="movie-provider">
          <div class="movie-provider-title">Stream Now</div>
          <div>
            <span
              class="movie-provider-logo"
              v-for="(provider, index) in movieData.providers" :key="`provider-${index}`"
              >
              <img class="movie-provider-logo-img" :src="`https://image.tmdb.org/t/p/original${provider.logo_path}`" alt="">
              {{ provider.name }}
            </span>
          </div>
        </div>
      </div>
      <div>
        <p v-if="movieData.tagline" class="movie-release-tagline">"{{ movieData.tagline }}"</p>
        <p class="movie-release-overview">{{ movieData.overview }}</p>
      </div>
      <!-- 예고편 스와이퍼 -->
      <movie-detail-video-swiper id="detail-video-swiper" :video-data="movieData.videos"/>
      <movie-detail-director-swiper id="detail-profile-swiper" :director-data="movieData.directors"/>
      <movie-detail-actor-swiper  id="detail-profile-swiper" :actor-data="movieData.actors"/>

      <div class="row">review comment 자리</div>
    </div>
    <!-- 배경이미지 -->
    <div id="backdrop">
      <div id="backdrop-cover"></div>
      <div id="backdrop-img"
        :style="`background-image: url('https://image.tmdb.org/t/p/w1280${ movieData.backdrop_path }');`">
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieDetailVideoSwiper from './MovieDetailVideoSwiper.vue'
import MovieDetailHeader from './MovieDetailHeader.vue'
import MovieDetailDirectorSwiper from './MovieDetailDirectorSwiper.vue'
import MovieDetailActorSwiper from './MovieDetailActorSwiper.vue'

export default {
  components: { MovieDetailVideoSwiper, MovieDetailHeader, MovieDetailDirectorSwiper, MovieDetailActorSwiper },
  name: 'MovieDetail',
  data() {
    return {
      movieData: {}
    }
  },
  mounted() {
    const movie_id = this.$route.query.movie_id
    const API_URL = 'http://127.0.0.1:8000'
    const Token = this.$store.state.token
    console.log(`Token ${Token}`)
    axios({
      method: 'GET',
      url: `${API_URL}/api/v1/movie/${movie_id}/`,
      headers: {
        Authorization: `Token ${Token}`
      }
    })
      .then((res) =>{
        console.log(res.data)
        this.movieData = res.data
      })
      .catch((err) =>{
        console.log(err)
      })
  }
}
</script>
<style lang="scss" scoped>
  @import './MovieDetail.scss';
</style>



