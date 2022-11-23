<template>
  <div>
    <div class="mypage">
      <my-page-analysis @rated-movies="ratedMovies" class="mypage-analysis"/>
      <user-follow/>
      <my-page-rating :rated-movie-data=ratedMovieData class="mypage-rating"/>
      <my-page-review/>
      <sign-out/>
    </div>
  </div>
</template>

<script>
import MyPageAnalysis from '../components/MyPageAnalysis.vue'
import MyPageRating from '../components/MyPageRating.vue'
import MyPageReview from '../components/MyPageReview.vue'
import UserFollow from '../components/UserFollow.vue'

//회원 탈퇴
import SignOut from '../components/SignOut.vue'

export default {
  components: { MyPageAnalysis, MyPageRating, MyPageReview, UserFollow, SignOut},
  name: 'MyPageView',
  computed: {
    userInfo() {
      return this.$store.state.username
    },
  },
  data() {
    return {
      ratedMovieData: {}
    }
  },
  methods: {
    ratedMovies(ratedMovieData) {
      this.ratedMovieData = ratedMovieData
    },
  },
  mounted() {
    console.log(window.location.pathname.replaceAll('/mypage/', ''))
  }
}

</script>

<style lang="scss" scoped>
@import "./MyPageView.scss";
</style>