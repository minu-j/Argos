<template>
  <div>
    <div class="mypage">
      <my-page-analysis @rated-movies="ratedMovies" class="mypage-analysis"/>
      <my-page-rating :rated-movie-data=ratedMovieData class="mypage-rating"/>
    </div>
  </div>
</template>

<script>
import MyPageAnalysis from '../components/MyPageAnalysis.vue'
import MyPageRating from '../components/MyPageRating.vue'

export default {
  components: { MyPageAnalysis, MyPageRating },
  name: 'MyPageView',
  computed: {
    userInfo() {
      return this.$store.state.username
    }
  },
  data() {
    return {
      ratedMovieData: {}
    }
  },
  methods: {
    ratedMovies(ratedMovieData) {
      this.ratedMovieData = ratedMovieData
    }
  }
}

</script>

<style lang="scss" scoped>
@import "./MyPageView.scss";
</style>