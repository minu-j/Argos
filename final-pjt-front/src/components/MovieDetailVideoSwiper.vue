<template>
  <div>
    <div class="swiper-title">
      <span class="swiper-title--item">이 영화의 예고편</span>
      <span class="swiper-title--item-count">{{videoData.length}}개</span>
    </div>
    <!-- 가로 스크롤 카드 스와이퍼 -->
    <div class="swiper">
      <swiper class="swiper-detail-row" :options="swiperOption">
        <swiper-slide v-for="(video, index) in videoData" :key="`movie-${index}`">
          <a :href="'https://youtu.be/' + video.key" target="_blank" class="movie-card">
            <span class="movie-card--title">{{ video.name }}</span>
            <img class="movie-card--thumbnail" :src="`https://img.youtube.com/vi/${ video.key }/mqdefault.jpg`">
          </a>
        </swiper-slide>
      </swiper>
    </div>
  </div>
</template>

<script>
  import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
  import 'swiper/css/swiper.css'
  export default {
    name: 'MovieDetailVideoSwiper',
    components: {
      Swiper,
      SwiperSlide
    },
    props: {
      videoData: Array,
    },
    data() {
      return {
        swiperOption: {
          slidesPerView: 2.5,
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

<style lang="scss">
  @import './MovieDetailVideoSwiper.scss';
</style>