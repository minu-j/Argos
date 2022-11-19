<template>
  <div>
    <div class="swiper-title">
      <span class="swiper-title--item">감독</span>
    </div>
    <!-- 가로 스크롤 카드 스와이퍼 -->
    <div class="swiper">
      <swiper class="swiper-detail-row" :options="swiperOption">
        <swiper-slide v-for="(director, index) in directorData" :key="`movie-${index}`">
          <div @click="goDetail(director.key)" class="movie-card">
            <span class="movie-card--title">{{ director.name }}</span>
            <img class="movie-card--thumbnail" :src="`https://image.tmdb.org/t/p/w500${ director.profile_path }`">
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
    name: 'MovieDetailDirectorSwiper',
    components: {
      Swiper,
      SwiperSlide
    },
    props: {
      directorData: Array,
    },
    data() {
      return {
        swiperOption: {
          slidesPerView: 3.5,
          slidesPerGroup: 1,
          loop: false,
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        },
      }
    },
  }
</script>

<style lang="scss" scoped>
  @import './MovieDetailDirectorSwiper.scss';
</style>