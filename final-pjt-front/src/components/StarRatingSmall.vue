<template>
  <span>
    <span v-if="!score.length">
      <svg :id="`star-1-${movieData.id}`" @click="createRating(1)" @mouseover="getGold(1)" @mouseleave="clearGold" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="#eee" :class="`star-${movieData.id}`"><g><path d="M12 17.444l-6.031 4.402c-.51.372-1.198-.128-1.001-.727l2.323-7.097L1.24 9.647c-.511-.37-.248-1.179.383-1.177l7.467.016 2.292-7.106c.193-.6 1.043-.6 1.237 0l2.292 7.106 7.467-.016c.63-.002.893.807.382 1.177l-6.05 4.375 2.322 7.097c.197.6-.491 1.1-1.001.727L12 17.444z"></path></g></svg>
      <svg :id="`star-2-${movieData.id}`" @click="createRating(2)" @mouseover="getGold(2)" @mouseleave="clearGold" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="#eee" :class="`star-${movieData.id}`"><g><path d="M12 17.444l-6.031 4.402c-.51.372-1.198-.128-1.001-.727l2.323-7.097L1.24 9.647c-.511-.37-.248-1.179.383-1.177l7.467.016 2.292-7.106c.193-.6 1.043-.6 1.237 0l2.292 7.106 7.467-.016c.63-.002.893.807.382 1.177l-6.05 4.375 2.322 7.097c.197.6-.491 1.1-1.001.727L12 17.444z"></path></g></svg>
      <svg :id="`star-3-${movieData.id}`" @click="createRating(3)" @mouseover="getGold(3)" @mouseleave="clearGold" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="#eee" :class="`star-${movieData.id}`"><g><path d="M12 17.444l-6.031 4.402c-.51.372-1.198-.128-1.001-.727l2.323-7.097L1.24 9.647c-.511-.37-.248-1.179.383-1.177l7.467.016 2.292-7.106c.193-.6 1.043-.6 1.237 0l2.292 7.106 7.467-.016c.63-.002.893.807.382 1.177l-6.05 4.375 2.322 7.097c.197.6-.491 1.1-1.001.727L12 17.444z"></path></g></svg>
      <svg :id="`star-4-${movieData.id}`" @click="createRating(4)" @mouseover="getGold(4)" @mouseleave="clearGold" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="#eee" :class="`star-${movieData.id}`"><g><path d="M12 17.444l-6.031 4.402c-.51.372-1.198-.128-1.001-.727l2.323-7.097L1.24 9.647c-.511-.37-.248-1.179.383-1.177l7.467.016 2.292-7.106c.193-.6 1.043-.6 1.237 0l2.292 7.106 7.467-.016c.63-.002.893.807.382 1.177l-6.05 4.375 2.322 7.097c.197.6-.491 1.1-1.001.727L12 17.444z"></path></g></svg>
      <svg :id="`star-5-${movieData.id}`" @click="createRating(5)" @mouseover="getGold(5)" @mouseleave="clearGold" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="#eee" :class="`star-${movieData.id}`"><g><path d="M12 17.444l-6.031 4.402c-.51.372-1.198-.128-1.001-.727l2.323-7.097L1.24 9.647c-.511-.37-.248-1.179.383-1.177l7.467.016 2.292-7.106c.193-.6 1.043-.6 1.237 0l2.292 7.106 7.467-.016c.63-.002.893.807.382 1.177l-6.05 4.375 2.322 7.097c.197.6-.491 1.1-1.001.727L12 17.444z"></path></g></svg>
    </span>
    <span v-if="score.length" @click="clearRating" @mouseover="readyClearRating" @mouseleave="cancelReadyClearRating">
      <svg :class="`goldStar star-${movieData.id}`" v-for="(index) in score" :key="`score-${index}`" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="#ffed75"><g><path d="M12 17.444l-6.031 4.402c-.51.372-1.198-.128-1.001-.727l2.323-7.097L1.24 9.647c-.511-.37-.248-1.179.383-1.177l7.467.016 2.292-7.106c.193-.6 1.043-.6 1.237 0l2.292 7.106 7.467-.016c.63-.002.893.807.382 1.177l-6.05 4.375 2.322 7.097c.197.6-.491 1.1-1.001.727L12 17.444z"></path></g></svg>
      <svg :class="`grayStar star-${movieData.id}`" v-for="(index) in notScore" :key="`notScore-${index}`" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="#eee"><g><path d="M12 17.444l-6.031 4.402c-.51.372-1.198-.128-1.001-.727l2.323-7.097L1.24 9.647c-.511-.37-.248-1.179.383-1.177l7.467.016 2.292-7.106c.193-.6 1.043-.6 1.237 0l2.292 7.106 7.467-.016c.63-.002.893.807.382 1.177l-6.05 4.375 2.322 7.097c.197.6-.491 1.1-1.001.727L12 17.444z"></path></g></svg>
    </span>
  </span>
</template>

<script>
import axios from 'axios'

export default {
  name: 'StarRating',
  data() {
    return {
      score: [],
      notScore: [1, 2, 3, 4, 5],
      scoreId: null
    }
  },
  props: {
    movieData: Object,
  },
  methods: {
    createRating(n) {  // 별 클릭시 별점 등록
      const movie_id = this.movieData.id
      const API_URL = 'http://127.0.0.1:8000'
      const Token = this.$store.state.token
      console.log(n)
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movie/${movie_id}/rating/`,
        headers: {
          Authorization: `Token ${Token}`
        },
        data: { score: n }
      })
        .then((res) => {
          this.scoreId = res.data.id
          console.log(res)
          this.rating(n)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    rating(n) {  // 사용자의 별점에 따라 별 생성하는 함수
      for (let i = 1; i < n + 1; i++) {
        const star = document.querySelector(`#star-${i}-${this.movieData.id}`)
        star.removeAttribute('fill')
        star.setAttribute('fill', "#ffed75")
        this.score.push(i)
        this.notScore.pop()
      }
    },
    getGold(n) {  // 마우스 오버시 별 노란색으로 채우기
      for (let i = 1; i < n + 1; i++) {
        const star = document.querySelector(`#star-${i}-${this.movieData.id}`)
        star.setAttribute('fill', "#ffed75")
      }
    },
    clearGold() {  // 마우스 벗어나면 별 초기화
      for (let i = 1; i < 6; i++) {
        const star = document.querySelector(`#star-${i}-${this.movieData.id}`)
        star.setAttribute('fill', "#eee")
      }
    },
    readyClearRating() {  // 마우스 올리면 별 색깔 희미하게 하기
      const goldStars = document.querySelectorAll(`.goldStar-${this.movieData.id}`)
      goldStars.forEach((goldStar) => {
        goldStar.removeAttribute('fill')
        goldStar.setAttribute('fill', "#f5eebf")
      })
    },
    cancelReadyClearRating() {  // 마우스 벗어나면 색깔 다시 돌아오기
      const goldStars = document.querySelectorAll(`.goldStar-${this.movieData.id}`)
      goldStars.forEach((goldStar) => {
        goldStar.removeAttribute('fill')
        goldStar.setAttribute('fill', "#ffed75")
      })
    },
    clearRating() {  // 이미 스코어가 있는 상태에서 별을 누르면 별점 취소하기
      const API_URL = 'http://127.0.0.1:8000'
      const rating_id = this.scoreId
      console.log(rating_id)
      this.score = []
      this.notScore = [1, 2, 3, 4, 5]
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/rating/${rating_id}/`,
      })
        .then(res => {
          console.log('별점 삭제', res)
        })
        .catch(err => {
          console.log('별점이 삭제되지 않았습니다.', err)
        })
    }
  },
  mounted() {
    const API_URL = 'http://127.0.0.1:8000'
    const user_id = this.$store.state.userId
    const movie_id = this.movieData.id
    axios({
      method: 'get',
      url: `${API_URL}/accounts/rating/${movie_id}/${user_id}/`,
    })
      .then(res => {
        const score = res.data.score
        this.scoreId = res.data.id
        this.rating(score)
      })
      .catch(err => {
        console.log('별점이 입력되지 않았습니다.', err)
      })
  }
}
</script>

<style scoped>
.star {
}
.star:hover {
  cursor: pointer;
}
</style>