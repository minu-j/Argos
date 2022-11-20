<template>
  <div>
      {{ratedMovieData}}
    <div class="rating">
      <div class="rating-title">내가 평가한 영화</div>
      <div v-for="(ratedMovie, index) in ratedMovieData" :key="`rated-movie-${index}`" class="rating-row">
        <span class="rating-rating">
          <span class="rating-rating-goldstar">★{{6 - index}}</span>
          <span>0개</span>
        </span>
        <my-page-rating-swiper/>
      </div>
    </div>
  </div>
</template>

<script>
import MyPageRatingSwiper from './MyPageRatingSwiper.vue'
export default {
  components: { MyPageRatingSwiper },
  name: 'MyPageRating',
  props: {
    ratedMovieData: Object,
  }
}
</script>

<style lang="scss" scoped>
  @import './MyPageRating.scss';
</style>