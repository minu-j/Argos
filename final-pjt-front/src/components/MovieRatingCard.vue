<template>
  <div>
    <div id="card">
      <div id="card-box">
        <star-rating-small id="card-star" :movie-data="randomMovie"/>
        <img :src="`https://image.tmdb.org/t/p/w500${randomMovie.poster_path}`" id="card-img" alt="">
      </div>
      <div id="card-title">{{ randomMovie.title }}</div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'

import StarRatingSmall from "./StarRatingSmall.vue"

export default {
  components: { StarRatingSmall },
  name: 'MovieRatingCard',
  props: {
    randomMovie: Object,
  },
  }
</script>

<style lang="scss" scoped>
  @import './MovieRatingCard.scss';
</style>