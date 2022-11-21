<template>
  <span class="star-box">
    <span v-if="!score.length">
      <svg :id="`star-1-${movieData.id}`" @click="createRating(1)" @mouseover="getGold(1)" @mouseleave="clearGold" xmlns="http://www.w3.org/2000/svg" width="44" height="44" fill="#eee" class="star"><g><path d="M22 33.444L9.83 42.327c-.784.572-1.842-.196-1.539-1.118l4.687-14.32L.769 18.06c-.787-.569-.383-1.812.588-1.81l15.067.033 4.624-14.34c.298-.924 1.606-.924 1.904 0l4.624 14.34 15.067-.033c.971-.002 1.375 1.241.588 1.81l-12.209 8.829 4.688 14.32c.302.922-.756 1.69-1.54 1.118L22 33.444z"></path></g></svg>
      <svg :id="`star-2-${movieData.id}`" @click="createRating(2)" @mouseover="getGold(2)" @mouseleave="clearGold" xmlns="http://www.w3.org/2000/svg" width="44" height="44" fill="#eee" class="star"><g><path d="M22 33.444L9.83 42.327c-.784.572-1.842-.196-1.539-1.118l4.687-14.32L.769 18.06c-.787-.569-.383-1.812.588-1.81l15.067.033 4.624-14.34c.298-.924 1.606-.924 1.904 0l4.624 14.34 15.067-.033c.971-.002 1.375 1.241.588 1.81l-12.209 8.829 4.688 14.32c.302.922-.756 1.69-1.54 1.118L22 33.444z"></path></g></svg>
      <svg :id="`star-3-${movieData.id}`" @click="createRating(3)" @mouseover="getGold(3)" @mouseleave="clearGold" xmlns="http://www.w3.org/2000/svg" width="44" height="44" fill="#eee" class="star"><g><path d="M22 33.444L9.83 42.327c-.784.572-1.842-.196-1.539-1.118l4.687-14.32L.769 18.06c-.787-.569-.383-1.812.588-1.81l15.067.033 4.624-14.34c.298-.924 1.606-.924 1.904 0l4.624 14.34 15.067-.033c.971-.002 1.375 1.241.588 1.81l-12.209 8.829 4.688 14.32c.302.922-.756 1.69-1.54 1.118L22 33.444z"></path></g></svg>
      <svg :id="`star-4-${movieData.id}`" @click="createRating(4)" @mouseover="getGold(4)" @mouseleave="clearGold" xmlns="http://www.w3.org/2000/svg" width="44" height="44" fill="#eee" class="star"><g><path d="M22 33.444L9.83 42.327c-.784.572-1.842-.196-1.539-1.118l4.687-14.32L.769 18.06c-.787-.569-.383-1.812.588-1.81l15.067.033 4.624-14.34c.298-.924 1.606-.924 1.904 0l4.624 14.34 15.067-.033c.971-.002 1.375 1.241.588 1.81l-12.209 8.829 4.688 14.32c.302.922-.756 1.69-1.54 1.118L22 33.444z"></path></g></svg>
      <svg :id="`star-5-${movieData.id}`" @click="createRating(5)" @mouseover="getGold(5)" @mouseleave="clearGold" xmlns="http://www.w3.org/2000/svg" width="44" height="44" fill="#eee" class="star"><g><path d="M22 33.444L9.83 42.327c-.784.572-1.842-.196-1.539-1.118l4.687-14.32L.769 18.06c-.787-.569-.383-1.812.588-1.81l15.067.033 4.624-14.34c.298-.924 1.606-.924 1.904 0l4.624 14.34 15.067-.033c.971-.002 1.375 1.241.588 1.81l-12.209 8.829 4.688 14.32c.302.922-.756 1.69-1.54 1.118L22 33.444z"></path></g></svg>
    </span>
    <span v-if="score.length" @click="clearRating" @mouseover="readyClearRating" @mouseleave="cancelReadyClearRating">
      <svg class="goldStar star" v-for="(index) in score" :key="`score-${index}`" xmlns="http://www.w3.org/2000/svg" width="44" height="44" fill="#ffed75"><g><path d="M22 33.444L9.83 42.327c-.784.572-1.842-.196-1.539-1.118l4.687-14.32L.769 18.06c-.787-.569-.383-1.812.588-1.81l15.067.033 4.624-14.34c.298-.924 1.606-.924 1.904 0l4.624 14.34 15.067-.033c.971-.002 1.375 1.241.588 1.81l-12.209 8.829 4.688 14.32c.302.922-.756 1.69-1.54 1.118L22 33.444z"></path></g></svg>
      <svg class="grayStar star" v-for="(index) in notScore" :key="`notScore-${index}`" xmlns="http://www.w3.org/2000/svg" width="44" height="44" fill="#eee"><g><path d="M22 33.444L9.83 42.327c-.784.572-1.842-.196-1.539-1.118l4.687-14.32L.769 18.06c-.787-.569-.383-1.812.588-1.81l15.067.033 4.624-14.34c.298-.924 1.606-.924 1.904 0l4.624 14.34 15.067-.033c.971-.002 1.375 1.241.588 1.81l-12.209 8.829 4.688 14.32c.302.922-.756 1.69-1.54 1.118L22 33.444z"></path></g></svg>
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
      scoreId: null,
      scoreData: null
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
          this.rating(n)
          this.scoreData = this.score.length
          this.$emit('user-score', this.scoreData)
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
      const goldStars = document.querySelectorAll('.goldStar')
      goldStars.forEach((goldStar) => {
        goldStar.removeAttribute('fill')
        goldStar.setAttribute('fill', "#f5eebf")
      })
    },
    cancelReadyClearRating() {  // 마우스 벗어나면 색깔 다시 돌아오기
      const goldStars = document.querySelectorAll('.goldStar')
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
        this.scoreData = this.score.length
        this.$emit('user-score', this.scoreData)
      })
      .catch(err => {
        console.log('별점이 입력되지 않았습니다.', err)
      })
  }
}
</script>

<style scoped>
.star {
  margin-right: 5px;
}
.star:hover {
  cursor: pointer;
}
</style>