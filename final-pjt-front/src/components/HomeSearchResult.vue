<template>
  <div>
    <div id="movie-search">
      <div v-if="searchInputData" class="movie-search--info">
        "{{searchInputData}}"의 검색결과 {{ searchResultData.length }} 건
      </div>
      <div v-else>검색어를 입력해주세요</div>
    </div>
    <div v-if="selectMovieData">
      <div id="movie-search-select" :style="`background-image: linear-gradient(rgba(0, 0, 0, 0.527), rgba(0, 0, 0, 0.5)), url(https://image.tmdb.org/t/p/w1280${selectMovieData.backdrop_path});`">
        <img @click="closeMovieDetail" src="@/assets/CloseIcon.png">
        <div id="movie-search-select-description">
          <div id="movie-search-select-title">{{ selectMovieData.title }}</div>
          <div id="movie-search-select-original_title">{{ selectMovieData.original_title }}</div>
          <div id="movie-search-select-vote_average">★ - {{ selectMovieData.vote_average }}</div>
          <div id="movie-search-select-release_date">{{ selectMovieData.release_date }}</div>
          <div id="movie-search-select-overview">{{ selectMovieData.overview }}</div>
          <a id="movie-search-select-more"  :href="`https://www.themoviedb.org/movie/${ selectMovieData.id }?language=ko`" target="_blank">더 보기</a>
        </div>
      </div>
    </div>
    <div v-if="searchResultData.length > 0" id="movie-search-result">
      <div class="container text-center" id="movie-search-result-container">
        <div class="row" id="movie-search-result-row">
          <div v-for="(movie, index) in searchResultData" :key="`search-${index}`" class="col-6 col-sm-4 col-lg-3">
            <div @click="openMovieDetail(movie)" id="movie-search-result-card">
              <div id="movie-search-result-card-box">
                <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" id="movie-search-result-card-img" alt="">
              </div>
              <div id="movie-search-result-card-title">{{ movie.title }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomeSearchResult',
  props: {
    searchInputData: String
  },
  data() {
    return {
      selectMovieData: null,
      searchResultData: []
    }
  },
  watch: {
    searchInputData: function() {
      this.searchResult()
    }
  },
  methods: {
    // 검색결과 출력
    searchResult() {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/search/movie?query=${this.searchInputData}&api_key=${process.env.VUE_APP_TMDB_API_KEY}&language=ko-KR&page=1`,
      })
        .then((res) => {
          // 인기도 순 출력
          const searchResultData = res.data.results.sort((a, b) => {
            if (a.popularity < b.popularity) {
              return 1
            } else if (a.popularity > b.popularity) {
              return -1
            }
          })
          this.searchResultData = searchResultData
          console.log(searchResultData)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    openMovieDetail(selectMovieData) {
      this.selectMovieData = selectMovieData
    },
    closeMovieDetail() {
      this.selectMovieData = null
    }
  },
}
</script>

<style lang="scss" scoped>
  @import './HomeSearchResult.scss';
</style>