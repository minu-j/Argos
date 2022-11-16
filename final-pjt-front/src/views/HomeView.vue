<template>
  <div>
    <home-movie/>
  </div>
</template>

<script>
import HomeMovie from '@/components/HomeMovie.vue'
export default {
  components: { HomeMovie },
  name: 'HomeView',
}
</script>

<style lang="scss">
@import "./HomeView.scss";
</style>