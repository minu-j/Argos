<template>
  <div>
    <div id="review-container" class="container">
      <div id="review-title">{{ userName }}님이 작성한 리뷰 {{reviewData.length}}개</div>
      <div id="review-row" class="row">
        <div v-for="(review, index) in [...reviewData].reverse()" :key="`review-${index}`" class="col-12 col-sm-6 col-lg-4 review">
          <div @click="goMovie(review.movie.id)" class="review-box">
            <div>
              <span class="review-gold" v-for="(goldstar, index) in review.score" :key="`goldstar-${index}`">★</span>
              <span class="review-silver" v-for="(silverstar, index) in 5 - review.score" :key="`silverstar-${index}`">★</span>
            </div>
            <div>
              <div class="review-content-small">{{review.content}}</div>
            </div>
            <div class="review-content-movie">
              {{review.movie.title}}
            </div>
            <div class="review-create">
              <span>{{review.created_at.slice(0, 10)}}</span>
              <span> · 댓글 {{ review.comment_set.length }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MyPageReview',
  data() {
    return {
      userName: null,
      reviewData: {}
    }
  },
  methods: {
    goMovie(id) {
      this.$router.push(`/movie/${id}`)
    }
  },
  mounted() {
    this.userName = window.location.pathname.replaceAll('/mypage/', '')
    const API_URL = 'http://127.0.0.1:8000'
    const Token = this.$store.state.token
    axios({
      method: 'GET',
      url: `${API_URL}/accounts/review/${this.userName}/`,
      headers: {
        Authorization: `Token ${Token}`
      }
    })
      .then((res) =>{
        console.log(res.data)
        this.reviewData = res.data
      })
      .catch((err) =>{
        console.log(err)
      })
  }
}
</script>

<style lang="scss" scoped>
  @import './MyPageReview.scss';
</style>