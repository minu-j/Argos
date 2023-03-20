<template>
  <div>
    <div id="rating">
      <div @click="goHome" id="exit">그만 평가할래요</div>
      <div id="rating-container">영화를 많이 평가할수록 더 많은 영화를 추천받을 수 있습니다.</div>
      <div class="container text-center">
        <div class="row">
          <div 
            v-for="(movie, index) in randomMovie"
            :key="`random-${index}`"
            class="col-6 col-sm-4 col-md-3 col-xl-2">
            <movie-rating-card :random-movie="movie"/>
          </div>
        </div>
        <div class="row" id="get-next-row">
            <div 
              v-for="loader in 24"
              :key="`loader-${loader}`"
              class="col-6 col-sm-4 col-md-3 col-xl-2">
              <movie-loader-card/>
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieRatingCard from './MovieRatingCard.vue'
import MovieLoaderCard from './MovieLoaderCard.vue'

  export default {
  components: { MovieRatingCard, MovieLoaderCard },
    name: 'MovieRating',
    data() {
      return {
        randomMovie: [],
      }
    },
    methods: {
      getNextMovie() {
        const API_URL = 'http://127.0.0.1:8000'
        const Token = this.$store.state.token
        axios({
          method: 'GET',
          url: `${API_URL}/api/v1/movie/random/`,
          headers: {
            Authorization: `Token ${Token}`
          }
        })
          .then((res) =>{
            console.log('영화 로드됨', res.data)
            res.data.data.forEach(element => {
              this.randomMovie.push(element)
            });
          })
          .catch((err) =>{
            console.log(err)
          })
      },
      goHome() {
        this.$router.push({ name: 'HomeView' })
      }
    },
    mounted() {
      const API_URL = 'http://127.0.0.1:8000'
      const Token = this.$store.state.token
      axios({
        method: 'GET',
        url: `${API_URL}/api/v1/movie/random/`,
        headers: {
          Authorization: `Token ${Token}`
        }
      })
        .then((res) =>{
          this.randomMovie = res.data.data

          // 로더 띄우기 용 감시 옵저버
          const target = document.querySelector('#get-next-row').firstChild
          console.log(target)

          const showLastMovie = (entries) => {

            // Destructuring
            const [{isIntersecting}] = entries;
            
            if (isIntersecting) {
              console.log('!!!', isIntersecting)
              this.getNextMovie()
            }
          };

          // intersection observer 생성자 초기화 (관찰자)
          const io = new IntersectionObserver(showLastMovie, {
            root: null,
            threshold: 0.5,
          })

          // NodeList의 각 요소들 감시 시작
          io.observe(target);

        })
        .catch((err) =>{
          console.log(err)
        })
    },
    
  }
</script>

<style lang="scss" scoped>
  @import './MovieRating.scss';
</style>