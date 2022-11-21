<template>
  <div>
    <div id="movie-swiper-title">
      <div id="movie-swiper-title-box">
        <div id="movie-swiper-title-box--item">{{ recommendMovies.prefix }} "{{ recommendMovies.name }}" {{ recommendMovies.category }}의 영화</div>
      </div>
    </div>
    <!-- 가로 스크롤 카드 스와이퍼 -->
    <div id="movie-swiper">
      <swiper id="movie-swiper-row" :options="swiperOption">
        <swiper-slide v-for="(movie, index) in recommendMovies.movies" :key="`movie-${index}`">
          <div @click="goDetail(movie.pk)" id="movie-card">
            <span id="movie-card--title">{{ movie.title }}</span>
            <img id="movie-card--thumbnail" :src="`https://image.tmdb.org/t/p/w500${ movie.backdrop_path }`">
          </div>
        </swiper-slide>
      </swiper>
    </div>
  </div>
</template>

<script>
  import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
  import 'swiper/css/swiper.css'
  export default {
    name: 'MovieSwiper',
    components: {
      Swiper,
      SwiperSlide
    },
    data() {
      return {
        swiperOption: {
          slidesPerView: 5,
          slidesPerGroup: 1,
          loop: true,
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        },
      }
    },
    props: {
      recommendMovies: Object
    },
    methods: {
      goDetail(id) {
        this.$router.push({ name: 'MovieDetail', params: { movie_id: id }, query: {movie_id: id}})
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import './MovieSwiper.scss';
</style>