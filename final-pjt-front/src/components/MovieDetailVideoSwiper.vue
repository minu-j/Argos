<template>
  <div>
    <div class="video-swiper-title">
      <span class="video-swiper-title--item">이 영화의 예고편</span>
      <span class="video-swiper-title--item-count">{{videoData.length}}개</span>
    </div>
    <!-- 가로 스크롤 카드 스와이퍼 -->
    <div class="video-swiper">
      <swiper class="video-swiper-detail-row" :options="swiperOption">
        <swiper-slide v-for="(video, index) in videoData" :key="`movie-${index}`">
          <div @click="playVideo(video.key)" class="movie-card">
            <span class="movie-card--title">{{ video.name }}</span>
            <img class="movie-card--thumbnail" :src="`https://img.youtube.com/vi/${ video.key }/mqdefault.jpg`">
          </div>
        </swiper-slide>
      </swiper>
    </div>
    <div v-if="videoKey">
      <div id="video-player">
        <iframe 
          width="870" 
          height="490" 
          :src="`https://www.youtube-nocookie.com/embed/${videoKey}?showinfo=0&modestbranding=1&rel=0&autoplay=1&fs=1`" 
          title="YouTube video player" 
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        >
        </iframe>
      </div>
      <div @click="closeVideo" id="bg"></div>
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
        videoKey: null
      }
    },
    methods: {
      playVideo(key) {
        this.videoKey = key
      },
      closeVideo() {
        this.videoKey = null
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import './MovieDetailVideoSwiper.scss';
</style>