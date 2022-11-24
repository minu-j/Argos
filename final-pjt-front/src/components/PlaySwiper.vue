<template>
  <div>
    <div id="gradient-right"></div>
    <div id="play-swiper-title">
      <div id="play-swiper-title-box">
        <div id="play-swiper-title-box--item">{{playList.title}}</div>
      </div>
    </div>
    <!-- 가로 스크롤 카드 스와이퍼 -->
    <div id="play-swiper">
      <swiper id="play-swiper-row" :options="swiperOption">
        <swiper-slide v-for="(videos, index) in playList.videos" :key="`videos-${index}`">
          <!-- {{videos}} -->
          <div @click="goDetail(videos.key)" id="play-card">
            <span id="play-card--title">{{ videos.title }}</span>
            <img id="play-card--thumbnail" :src="`https://img.youtube.com/vi/${ videos.key }/mqdefault.jpg`">
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
    name: 'PlaySwiper',
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
      }
    },
    props: {
      playList: Object
    },
    methods: {
      goDetail(key) {
        this.$router.push(`/play/${key}`)
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import './PlaySwiper.scss';
</style>