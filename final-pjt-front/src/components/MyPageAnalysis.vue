<template>
  <div>
    <div v-if="!isEmpty" class="analysis">
      <div class="analysis-desctiption">
        {{userName}}님이 평가하신 {{ userRating[1].length + userRating[2].length + userRating[3].length + userRating[4].length + userRating[5].length }}개 영화를 바탕으로 취향을 분석해봤어요.
      </div>
      <div class="analysis-title">선호하는 키워드</div>
      <div v-if="likeKeyword.length">
        <wordcloud
          :data="likeKeyword"
          nameKey="name"
          valueKey="value"
          :color="myColors"
          :showTooltip="false"
          font="Paytone One"
          :wordClick="wordClickHandler">
        </wordcloud>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-12 col-md-4">
            <div class="analysis-card">
              <div class="analysis-card-title">배우</div>
              <div v-for="(actor, index) in likeActor" :key="`actor-${index}`" class="analysis-card-content">
                <span class="analysis-card-content-name">{{ actor['0'] }}</span><span class="analysis-card-content-ratio">{{ actor['1'] }}%</span>
              </div>
            </div>
          </div>
          <div class="col-12 col-md-4">
            <div class="analysis-card">
              <div class="analysis-card-title">감독</div>
              <div v-for="(director, index) in likeDirector" :key="`director-${index}`" class="analysis-card-content">
                <span class="analysis-card-content-name">{{ director['0'] }}</span><span class="analysis-card-content-ratio">{{ director['1'] }}%</span>
              </div>
            </div>
          </div>
          <div class="col-12 col-md-4">
            <div class="analysis-card">
              <div class="analysis-card-title">장르</div>
              <div v-for="(genre, index) in likeGenre" :key="`genre-${index}`" class="analysis-card-content">
                <span class="analysis-card-content-name">{{ genre['0'] }}</span><span class="analysis-card-content-ratio">{{ genre['1'] }}%</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <my-page-analysis-graph :user-rating="userRating"/>
      <div v-if="userName === this.$store.state.username" id="offer-rating">
        더 많은 영화를 평가해보세요
        <div @click="goRating" id="offer-rating-link">본 영화 평가하러 가기 →</div>
      </div>
    </div>
    <div v-else id="offer-rating">
      앗! 아직 평가를 안하셨네요!
      <div @click="goRating" id="offer-rating-link">본 영화 평가하러 가기 →</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import wordcloud from 'vue-wordcloud'
import MyPageAnalysisGraph from './MyPageAnalysisGraph.vue'

export default {
  components: {
    wordcloud,
    MyPageAnalysisGraph,
  },
  name: 'MyPageAnalysis',
  data () {
    return {
      myColors: ['#DEE1E6', '#F1F3F4', '#BABCBE', '#535353'],
      userRating: {},
      likeActor: [],
      likeDirector: [],
      likeGenre: [],
      likeKeyword: [],
      isEmpty: false,
      userName: null
    }
  },
  methods: {
    wordClickHandler(name, value, vm) {
      console.log('wordClickHandler', name, value, vm);
    },
    goRating() {
      this.$router.push({ name:'MovieRating' })
    }
  },
  mounted() {
    // 유저의 영화취향 불러오기
    this.userName = window.location.pathname.replaceAll('/mypage/', '')
    const myName = this.$store.state.username
    const API_URL = this.$store.state.API_URL
    const Token = this.$store.state.token
    axios({
      method: 'GET',
      url: `${API_URL}/accounts/analysis/${this.userName}/`,
      headers: {
        Authorization: `Token ${Token}`
      }
    })
      .then((res) =>{
        console.log(res)
        this.likeActor = res.data.like_actor
        this.likeDirector = res.data.like_director
        this.likeGenre = res.data.like_genre
        this.likeKeyword = res.data.like_keyword
        this.userRating = res.data.rating
        this.$emit('rated-movies', this.userRating)
      })
      .catch((err) =>{
        console.log(err)
        // 내가 내 마이페이지 들어갔을 때 평가한 영화가 없다면
        if (myName === this.userName) {
          this.isEmpty = true  // 아무 영화도 평가를 안했으므로 평가 링크 권유
        } else {  // 없는 사람 링크로 들어간 경우 404
          this.$router.push({ name: 'NotFound404' })
        }
      })
  }
}
</script>

<style lang="scss" scoped>
  @import './MyPageAnalysis.scss';
</style>