<template>
  <div>
    <div id="movie-header" class="container">
      <!-- 상단 영화설명 -->
      <div class="movie row">
        <div class="col-10 col-md-4">
          <div>
            <img class="movie-poster" :src="`https://image.tmdb.org/t/p/w1280${movieData.poster_path}`" alt="">
          </div>
        </div>
        <!-- 영화 설명 컬럼 -->
        <div class="col-10 col-md-8 movie-header">
          <p class="movie-title ds-5">{{ movieData.title }}</p>
          <p class="movie-original_title">{{ movieData.original_title }}</p>
          <p class="movie-release_date">{{ movieData.release_date }} | {{ movieData.runtime }}분</p>
          <!-- 장르 클릭시 해당 장르 세부페이지 연결 -->
          <div class="movie-genre">
            <a v-for="(genre, index) in movieData.genres" :key="`genre-${index}`" 
              class="movie-genre-tag"
              @click="goDetail(genre)"
              href="#">
              {{ genre.name }}
            </a>
          </div>
          <!-- 별점 컨테이너 -->
          <star-rating @user-score="userScore" :movie-data="movieData"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import StarRating from './StarRating.vue'

export default {
  components: { StarRating },
  name: 'MovieDetailHeader',
  props: {
    movieData: Object,
  },
  data() {
    return {
      scoreData: null,
    }
  },
  methods: {
    goDetail(genre) {
      this.$emit('active-genre-modal', genre)
    },
    userScore(score) {
      this.scoreData = score
      this.$emit('user-score', score)
    }
  }
}
</script>

<style lang="scss" scoped>
  @import './MovieDetailHeader.scss';
</style>

