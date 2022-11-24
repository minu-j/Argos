<template>
  <div>
    <div id="gradient-right"></div>
    <div id="movie-swiper-title">
      <div id="movie-swiper-title-box">
        <div id="movie-swiper-title-box--item">{{ recommendMovies.prefix }} "{{ recommendMovies.name }}" {{ recommendMovies.category }}의 영화</div>
      </div>
    </div>
    <!-- 가로 스크롤 카드 스와이퍼 -->
    <div id="movie-swiper">
      <swiper id="movie-swiper-row" :options="swiperOption">
        <swiper-slide v-for="(movie, index) in recommendMovies.movies" :key="`movie-${index}`">
          <div @mouseover="videoPreview(movie.pk, movie.backdrop_path)" @mouseleave="stopPreview" @click="goDetail(movie.pk)" id="movie-card">
            <div id="movie-card-cover"  @click="goDetail(movie.pk)"></div>
            <iframe v-if="previewKey === movie.pk"
              width="256" 
              height="256" 
              :src="`https://www.youtube-nocookie.com/embed/${movie.videos['0'].key}?showinfo=0&modestbranding=1&rel=0&autoplay=1&fs=1&controls=0&disablekb=1&mute=1`" 
              title="YouTube video player" 
              frameborder="0" 
              allow="accelerometer; autoplay;" 
            >
            </iframe>
            <img id="movie-card--thumbnail" :src="`https://image.tmdb.org/t/p/w500${ movie.backdrop_path }`">
            <span id="movie-card--title">{{ movie.title }}</span>
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
          loop: false,
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        },
        previewKey: null,
      }
    },
    props: {
      recommendMovies: Object
    },
    methods: {
      goDetail(id) {
        this.$router.push(`/movie/${id}`)
      },
      videoPreview(key) {
        this.previewKey = key
      },
      stopPreview() {
        this.previewKey = null
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import './MovieSwiper.scss';
</style>