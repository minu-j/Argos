<template>
  <div>
    <home-boxoffice/>
    <home-search/>
    <home-movie-recommend/>
  </div>
</template>

<script>
import HomeBoxoffice from '../components/HomeBoxoffice.vue'
import HomeSearch from '../components/HomeSearch.vue'
import HomeMovieRecommend from '../components/HomeMovieRecommend.vue'

export default {
  components: { 
    HomeSearch, 
    HomeBoxoffice,
    HomeMovieRecommend,
  },
  name: 'HomeView',
}
</script>

<style lang="scss" scoped>
@import "./HomeView.scss";
</style>