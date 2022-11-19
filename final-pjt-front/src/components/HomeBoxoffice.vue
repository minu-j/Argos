<template>
  <div>
    <swiper class="swiper-row" :options="swiperOption"> 
      <swiper-slide v-for="(boxoffice, index) in boxofficeData" :key="`boxoffice-${index}`">
        <div>{{ boxoffice.rank }}위 {{boxoffice.movieNm}}</div>
        <div>관객 증감분 : {{ boxoffice.rankInten }}</div>
        <div>신규진입여부 : {{ boxoffice.rankOldAndNew }}</div>
        <div>관객점유율 : {{ boxoffice.salesChange }}</div>
        <div>일일 관객수 : {{ boxoffice.audiCnt }}</div>
        <div>누적 관객수 : {{ boxoffice.audiAcc }}</div>
      </swiper-slide>
    </swiper>
  </div>
</template>

<script>
import axios from 'axios'

  import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
  import 'swiper/css/swiper.css'
  export default {
    name: 'HomeBoxoffice',
    components: {
      Swiper,
      SwiperSlide
    },
  data() {
    return {
      swiperOption: {
        direction: "vertical",
        autoplay:{
          delay: 2500,
          disableOnInteraction: false,
        },
        slidesPerView: 1,
        slidesPerGroup: 1,
        loop: true,
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev'
        },
        avigation: true
      },
      boxofficeData: [],
    }
  },
  mounted() {
    const today = new Date()
    let year = today.getFullYear()
    let month = today.getMonth() + 1
    if (String(month).length === 1) {
      let month = '0' + month
    }
    let date = today.getDate() - 1
    if (String(date).length === 1) {
      let date = '0' + date
    }
    const todayDate = String(year) + String(month) + String(date)
    console.log(todayDate)

    const KOBIS_API_URL = 'https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
    console.log(`${KOBIS_API_URL}?key=${process.env.VUE_APP_KOBIS_API_KEY}&targetDt=${todayDate}`)

    axios({
      method: 'GET',
      url: `${KOBIS_API_URL}?key=${process.env.VUE_APP_KOBIS_API_KEY}&targetDt=${todayDate}`
    })
      .then((res) => {
        console.log(res.data)
        this.boxofficeData = res.data.boxOfficeResult.dailyBoxOfficeList
      })
      .catch((err) => {
        console.log(err)
      })
  }
}

</script>

<style lang="scss" scoped>
  @import './HomeBoxoffice.scss';
</style>