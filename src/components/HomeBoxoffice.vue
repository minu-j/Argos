<template>
  <div id=boxoffice>
    <swiper id="boxoffice-swiper-row" :options="swiperOption"> 
      <swiper-slide v-for="(boxoffice, index) in boxofficeData" :key="`boxoffice-${index}`">
        <div>
          <div>
            <span id="boxoffice-rank">{{ boxoffice.rank }}위</span>
            <!-- 새로 랭크된 경우 NEW 출력 -->
            <span v-if="boxoffice.rankOldAndNew === 'NEW'" id="boxoffice-new">{{ boxoffice.rankOldAndNew }}</span>
            <!-- 이미 랭크되어 있었을 경우 순위 출력 -->
            <span v-if="boxoffice.rankOldAndNew === 'OLD'" id="boxoffice-rank-change">
              <!-- 순위 상승 -->
              <span id="boxoffice-rank-change-up" v-if="boxoffice.rankInten > 0">
                <span id="boxoffice-rank-change-up--arrow">▲</span>
                <span id="boxoffice-rank-change-up--num">{{ boxoffice.rankInten }}</span>
              </span>
              <!-- 순위 하락 -->
              <span id="boxoffice-rank-change-down" v-if="boxoffice.rankInten < 0">
                <span id="boxoffice-rank-change-down--arrow">▼</span>
                <span id="boxoffice-rank-change-down--num">{{ boxoffice.rankInten.slice(1) }}</span>
              </span>
            </span>
          </div>
          <!-- 제목 -->
          <div id="boxoffice-title">{{ boxoffice.movieNm }}</div>
          <div>
            <!-- 점유율, 누적관객수, 일일관객수 -->
            <div id="boxoffice-share">{{ boxoffice.salesShare }}%</div>
            <span id="boxoffice-acc">{{ parseInt(boxoffice.audiAcc).toLocaleString('ko-KR') }}명</span>
            <span id="boxoffice-cnt">+ {{ parseInt(boxoffice.audiCnt).toLocaleString('ko-KR') }}</span>
          </div>
        </div>
      </swiper-slide>
    </swiper>
    <div id=boxoffice-info>
      <div id=boxoffice-info--text>
        <a href="https://www.kobis.or.kr/kobis/" target="_blank">{{ today.year }}년 {{ today.month }}월 {{ today.date }}일 KOBIS 영화관입장권통합전산망 기준</a>
      </div>
    </div>
    <div id="backdrop">
      <div id="backdrop-cover"></div>
      <div id="backdrop-img">
      </div>
    </div>
  </div>
</template>

<script>

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
          delay: 5000,
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
      today: {},
      boxofficeData: [],
      nowShowBoxoffice: null,
      boxOfficeImage: {},
      nowBoxOfficeImage: null
    }
  },
  watch: {
    // 출력되는 박스오피스 영화가 바뀔경우 배경 바꿔주기
    nowShowBoxoffice: function () {
      if (this.nowBoxOfficeImage === null) {
        this.boxOfficeImage = this.$store.state.boxOfficeImage
      }
      const boxofficeBg = document.querySelector('#backdrop-img')
      if (this.boxOfficeImage[this.nowShowBoxoffice]) {
        boxofficeBg.setAttribute('style', `background-image: url('https://image.tmdb.org/t/p/w1280/${this.boxOfficeImage[this.nowShowBoxoffice]}');`)
      } else {
        boxofficeBg.setAttribute('style', `background-image: url("${require(`@/assets/notBackgroundImage.png`)}");`)
      }
    }
  },
  mounted() {
    this.today = this.$store.state.todayDate
    this.boxofficeData = this.$store.state.boxofficeData
    this.boxOfficeImage = this.$store.state.boxOfficeImage

    // 배경 설정을 위해 지금 어떤 영화가 출력중인지 DOM 감지 : MutationObserver 사용
    const target = document.querySelector('#boxoffice-swiper-row')
    const observer = new MutationObserver(() => {
      const activeBoxoffice = document.querySelector('.swiper-slide-active #boxoffice-title')
      this.nowShowBoxoffice = activeBoxoffice.innerText
    })
    const config = {
      attributes: true,
      subtree: true
    }
    observer.observe(target, config);
  }
}

</script>

<style lang="scss" scoped>
  @import './HomeBoxoffice.scss';
</style>