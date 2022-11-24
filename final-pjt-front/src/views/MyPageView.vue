<template>
  <div>
    <div class="mypage">
      <div class="mypage-username">{{userName}}</div>
      <user-follow/>
      <my-page-analysis @rated-movies="ratedMovies" class="mypage-analysis"/>
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
      ratedMovieData: {},
      userName: null
    }
  },
  methods: {
    ratedMovies(ratedMovieData) {
      this.ratedMovieData = ratedMovieData
    },
  },
  mounted() {
    this.userName = window.location.pathname.replaceAll('/mypage/', '')
  }
}

</script>

<style lang="scss" scoped>
@import "./MyPageView.scss";
</style>