<template>
  <div>
    <div class="swiper-title">
      <div class="swiper-title--item">좋아하는 영화</div>
    </div>
    <div class="swiper">
      <swiper class="swiper-row" :options="swiperOption">
        <swiper-slide v-for="(movie, index) in movies" :key="`movie-${index}`">
          <div @click="goDetail(index)" class="movie-card">
            <span class="movie-card--title">{{ movie.title }}</span>
            <img class="movie-card--thumbnail" :src="`${ movie.thumbnail }`">
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
        movies: [ // dummy data
        {
          title: '기생충',
          thumbnail: 'https://img.sbs.co.kr/newimg/news/20190623/201326992_1280.jpg',
          videoId: 'jBdRhhSt3Bc',
        },
        {
          title: '모가디슈',
          thumbnail: 'https://cdn.mhns.co.kr/news/photo/202106/507026_611653_2147.jpg',
        },
        {
          title: '긴제목긴긴긴긴목이긴기긴긴기린목이긴기린제목',
          thumbnail: 'http://ojsfile.ohmynews.com/PHT_IMG_FILE/2018/0201/IE002279353_PHT.jpg',
        },
        {
          title: '1987',
          thumbnail: 'http://ojsfile.ohmynews.com/STD_IMG_FILE/2018/0108/IE002268886_STD.jpg',
        },
        {
          title: 'D.P.',
          thumbnail: 'https://img4.daumcdn.net/thumb/R658x0.q70/?fname=https://t1.daumcdn.net/news/202108/03/NEWS1/20210803095000690pbol.jpg',
        },
        {
          title: '수리남',
          thumbnail: 'http://woman.chosun.com/news/photo/202209/102404_93305_2622.jpg',
        },
      ],
      }
    },
    methods: {
      goDetail(id) {
        this.$router.push({ name: 'MovieDetail', params: { movie_id: id }})
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import './MovieSwiper.scss';
</style>