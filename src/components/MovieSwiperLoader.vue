<template>
  <div>
    <div id="gradient-left"></div>
    <div id="gradient-right"></div>
    <div id="movie-swiper-title">
      <div id="movie-swiper-title-box">
        <div id="movie-swiper-title-box--item">ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ</div>
      </div>
    </div>
    <!-- 가로 스크롤 카드 스와이퍼 -->
    <div id="movie-swiper">
      <swiper id="movie-swiper-row" :options="swiperOption">
        <swiper-slide v-for="i in 5" :key="`${i}`">
          <div id="movie-card">
            <img id="movie-card--thumbnail" src="@/assets/backdropLoader.png">
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
    name: 'MovieSwiperLoader',
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
  }
</script>

<style lang="scss" scoped>
  @import './MovieSwiperLoader.scss';
</style>