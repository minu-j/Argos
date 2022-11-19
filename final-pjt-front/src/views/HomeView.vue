<template>
  <div>
    <home-boxoffice/>
    <home-search/>
    <home-movie/>
  </div>
</template>

<script>
import HomeMovie from '@/components/HomeMovie.vue'
import HomeBoxoffice from '../components/HomeBoxoffice.vue'
import HomeSearch from '../components/HomeSearch.vue'

export default {
  components: { 
    HomeSearch, 
    HomeBoxoffice,
    HomeMovie,
  },
  name: 'HomeView',
}
</script>

<style lang="scss" scoped>
@import "./HomeView.scss";
</style>