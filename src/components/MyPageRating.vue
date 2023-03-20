<template>
  <div>
    <div class="rating">
      <div class="rating-title">{{ratedMovieData[5].length + ratedMovieData[4].length + ratedMovieData[3].length + ratedMovieData[2].length + ratedMovieData[1].length }}개의 영화를 평가했어요</div>
      <div v-if="ratedMovieData[5].length > 0" class="rating-row">
        <span class="rating-rating">
          <span class="rating-rating-goldstar">★★★★★</span>
          <span class="rating-rating-num">{{ ratedMovieData[5].length}}개</span>
        </span>
        <my-page-rating-swiper :rated-movie-data="ratedMovieData[5]"/>
      </div>
      <div v-if="ratedMovieData[4].length > 0" class="rating-row">
        <span class="rating-rating">
          <span class="rating-rating-goldstar">★★★★</span>
          <span class="rating-rating-silverstar">★</span>
          <span class="rating-rating-num">{{ ratedMovieData[4].length}}개</span>
        </span>
        <my-page-rating-swiper :rated-movie-data="ratedMovieData[4]"/>
      </div>
      <div v-if="ratedMovieData[3].length > 0" class="rating-row">
        <span class="rating-rating">
          <span class="rating-rating-goldstar">★★★</span>
          <span class="rating-rating-silverstar">★★</span>
          <span class="rating-rating-num">{{ ratedMovieData[3].length}}개</span>
        </span>
        <my-page-rating-swiper :rated-movie-data="ratedMovieData[3]"/>
      </div>
      <div v-if="ratedMovieData[2].length > 0" class="rating-row">
        <span class="rating-rating">
          <span class="rating-rating-goldstar">★★</span>
          <span class="rating-rating-silverstar">★★★</span>
          <span class="rating-rating-num">{{ ratedMovieData[2].length}}개</span>
        </span>
        <my-page-rating-swiper :rated-movie-data="ratedMovieData[2]"/>
      </div>
      <div v-if="ratedMovieData[1].length > 0" class="rating-row">
        <span class="rating-rating">
          <span class="rating-rating-goldstar">★</span>
          <span class="rating-rating-silverstar">★★★★</span>
          <span class="rating-rating-num">{{ ratedMovieData[1].length}}개</span>
        </span>
        <my-page-rating-swiper :rated-movie-data="ratedMovieData[1]"/>
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