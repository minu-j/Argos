<template>
  <div>
    <div id="movie-swiper-title">
      <div id="movie-swiper-title-box">
      </div>
    </div>
    <!-- 가로 스크롤 카드 스와이퍼 -->
    <div id="movie-swiper">
      <swiper id="movie-swiper-row" :options="swiperOption">
        <swiper-slide v-for="(movie, index) in ratedMovieData" :key="`movie-${index}`">
          <div @click="goDetail(movie.id)" id="movie-card">
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
    name: 'MyPageRatingSwiper',
    components: {
      Swiper,
      SwiperSlide
    },
    data() {
      return {
        swiperOption: {
          slidesPerView: 2,
          slidesPerGroup: 1,
          loop: false,
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        },
        swiperTitle: '지금 뜨는 영화',
        movieData: [],
      }
    },
    props: {
      ratedMovieData: Array
    },
    methods: {
      goDetail(id) {
        this.$router.push({ name: 'MovieDetail', params: { movie_id: id }, query: {movie_id: id}})
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import './MyPageRatingSwiper.scss';
</style>