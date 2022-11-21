<template>
  <div>
    {{userScore}}
    <div id="review-container" class="container">
      <div class="row">
        <div class="col-12 col-sm-6 col-lg-4">
          <div></div>
          <textarea name="" id="review-textarea" rows="5" placeholder="이 영화의 리뷰 작성"></textarea>
          <button>저장</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'MovieDetailReview',
  props: {
    movieData: Object,
    userScore: Number
  },
  methods: {
    // createReview() {
    //   const API_URL = 'http://127.0.0.1:8000'
    //   const movie_id = this.movieData.id
      
    //   axios({
    //     method: 'delete',
    //     url: `${API_URL}/api/v1/rating/${rating_id}/`,
    //   })
    //     .then(res => {
    //       console.log('별점 삭제', res)
    //     })
    //     .catch(err => {
    //       console.log('별점이 삭제되지 않았습니다.', err)
    //     })
    // }
  }
}
</script>

<style lang="scss" scoped>
  @import './MovieDetailReview.scss';
</style>