<template>
  <div>
    <div class="swiper-title">
      <span class="swiper-title--item">출연</span>
    </div>
    <!-- 가로 스크롤 카드 스와이퍼 -->
    <div class="swiper">
      <swiper class="swiper-detail-row" :options="swiperOption">
        <swiper-slide v-for="(actor, index) in actorData" :key="`movie-${index}`">
          <div @click="goDetail(actor)" class="movie-card">
            <span class="movie-card--title">{{ actor.name }}</span>
            <img class="movie-card--thumbnail" :src="`https://image.tmdb.org/t/p/w500${ actor.profile_path }`">
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
    name: 'MovieDetailActorSwiper',
    components: {
      Swiper,
      SwiperSlide
    },
    props: {
      actorData: Array,
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
    methods: {
      goDetail(actor) {
        this.$emit('active-actor-modal', actor)
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import './MovieDetailDirectorSwiper.scss';
</style>