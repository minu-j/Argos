<template>
  <div>
    <!-- 모달 -->
    <div v-show="modalActive" id="search-modal-search">
      <div id="search-modal-search-box">
        <img src="@/assets/ARGOS_logo.svg" alt="">
        <input 
          type="text" 
          @keyup="searchInput" 
          @keyup.esc="modalActiveTogle" 
          placeholder="SEARCH" 
          id="search-modal-search--input">
      </div>
      <div id="search-modal-search-result">
        <home-search-result :search-input-data="searchInputData"/>
      </div>
      <div v-show="modalActive" @click="modalActiveTogle" id="search-modal"></div>
    </div>
    <!-- 모달 배경 -->
    <div v-if="modalActive" @click="modalActiveTogle" id="search-modal--bg"></div>

    <!-- 홈화면에 보이는 검색창 -->
    <div id="home-search">
      <div id="home-search-box">
        <!-- 검색창은 비활성화 -->
        <img src="@/assets/ARGOS_logo.svg" alt="">
        <input @click="modalActiveTogle" placeholder="SEARCH" type="text" id="search--input" readonly>
      </div>
    </div>
  </div>
</template>

<script>
import HomeSearchResult from './HomeSearchResult.vue'
export default {
  components: { HomeSearchResult },
  name: 'HomeSearch',
  props: {
  },
  data() {
    return {
      modalActive: false, // 모달 표시여부
      ableSearch: true, // 검색해도 되는지 확인용
      searchInputData: null,  // 검색 데이터
    }
  },
  methods: {
    // 모달 배경을 누르거나, 서치 인풋태그를 누르면 모달 켜지거나 꺼지게 하는 함수
    modalActiveTogle() {
      this.modalActive = !this.modalActive

      // 애니메이션이 마쳐지기 전에 focus를 하면 적용이 안돼서, 200ms set time out 후 적용하기
      setTimeout(() => {
        const searchModalInputTag = document.querySelector('#search-modal-search--input')
        searchModalInputTag.focus()
      }, 200);
    },
    // 검색창 입력 감지 : v-model을 쓰면 한국어 입력 이슈가 있으므로 함수 처리
    searchInput() {
      // 너무 자주 검색되지 않도록 1초 간격으로 settimeout 설정
      if (this.ableSearch) {
        this.ableSearch = false  // 일정시간 자동검색 막기
        const searchModalInputTag = document.querySelector('#search-modal-search--input')
        setTimeout(() => {
          this.searchInputData = searchModalInputTag.value
          this.ableSearch = true
        }, 1000);
      }
    },
  },
}
</script>

<style lang="scss" scoped>
  @import './HomeSearch.scss';
</style>