<template>
  <div>
    <div class="movie container">
      <div class="row">
        <div class="col-6 col-xs-5 col-sm-4 col-md-3 col-lg-3">
          <div>
            <img class="movie-poster" :src="`https://image.tmdb.org/t/p/w1280${movie.fields.poster_path}`" alt="">
          </div>
        </div>
        <div class="col-12 col-md-9 movie-header">
          <p class="movie-title ds-5">{{ movie.fields.title }}</p>
          <p class="movie-original_title">{{ movie.fields.original_title }}</p>
          <p class="movie-release_date">{{ movie.fields.release_date }} | {{ movie.fields.runtime }}분</p>
          <star-rating/>
        </div>
      </div>
      <div class="row">
        <p class="movie-release-tagline">"{{ movie.fields.tagline }}"</p>
        <p class="movie-release-overview">{{ movie.fields.overview }}</p>
      </div>
    </div>
    <!-- 배경이미지 -->
    <div id="backdrop">
      <div id="backdrop-cover"></div>
      <div id="backdrop-img"
        :style="`background-image: url('https://image.tmdb.org/t/p/w1280${ movie.fields.backdrop_path }');`">
      </div>
    </div>
  </div>
</template>

<script>
import StarRating from './StarRating.vue'

export default {
  components: { StarRating },
  name: 'MovieDetail',
  data() {
    return {
      movie: { // dummy data
            "model": "movies.movie",
            "pk": 361743,
            "fields": {
              "title": "탑건: 매버릭",
              "original_title": "Top Gun: Maverick",
              "overview": "최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데...",
              "release_date": "2022-06-22",
              "popularity": 903.97,
              "vote_average": 8.3,
              "poster_path": "/jeqXUwNilvNqNXqAHsdwm5pEfae.jpg",
              "backdrop_path": "/AaV1YIdWKnjAIAOe8UUKBFm327v.jpg",
              "runtime": 131,
              "status": "Released",
              "tagline": "한순간의 실수도 용납되지 않는 하늘 위, 가장 압도적인 비행이 시작된다",
              "genres": [
                28,
                18
              ],
              "actors": [
                500,
                996701,
                6161
              ],
              "directors": [
                86270
              ],
              "keywords": [
                2533,
                4410,
                9663,
                160381,
                162365
              ],
              "videos": [
                "62b58d7fe33f83005127edd1",
                "62b58d84a3491100517c1d59",
                "62b58d981b722c0468996b4a",
                "62b58daaa34911008b7a86f3",
                "62b58da54f9a9900608bec9c",
                "629604200f21c615394fd490",
                "629604275507e9149747a479",
                "629603d3a44d090067bbda4d",
                "629603dc09ed8f125355a473",
                "6296042d0f21c615389952ae",
                "6296043409ed8f12555649b0",
                "6296044ba44d0900a98db2e8",
                "629603e109ed8f1255564904",
                "628ec6791a32483b6247bcf6",
                "62431104dfe31d00475a9785",
                "60339b1fc26796003ecd2547",
                "5dfa5648609750001532e6f6",
                "5d316db66a300b5922abf46e"
              ],
              "providers": []
            }      },
    }
  }
}
</script>

<style lang="scss" scoped>
  @import './MovieDetail.scss';
</style>