<template>
  <div>
    <div id="movie-swiper-title">
      <div id="movie-swiper-title-box">
      </div>
    </div>
    <!-- 가로 스크롤 카드 스와이퍼 -->
    <div id="movie-swiper">
      <swiper id="movie-swiper-row" :options="swiperOption">
        <swiper-slide v-for="(movie, index) in movieData" :key="`movie-${index}`">
          <div @click="goDetail(movie.pk)" id="movie-card">
            <span id="movie-card--title">{{ movie.fields.title }}</span>
            <img id="movie-card--thumbnail" :src="`https://image.tmdb.org/t/p/w500${ movie.fields.backdrop_path }`">
          </div>
        </swiper-slide>
      </swiper>
    </div>
  </div>
</template>

<script>
  import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
  import 'swiper/css/swiper.css'
  export default {
    name: 'MyPageRatingSwiper',
    components: {
      Swiper,
      SwiperSlide
    },
    data() {
      return {
        swiperOption: {
          slidesPerView: 5,
          slidesPerGroup: 1,
          loop: true,
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        },
        swiperTitle: '지금 뜨는 영화',
        movieData: [{
            "model": "movies.movie",
            "pk": 505642,
            "fields": {
              "title": "블랙 팬서: 와칸다 포에버",
              "original_title": "Black Panther: Wakanda Forever",
              "overview": "국왕이자 블랙 팬서인 티찰라의 죽음 이후 수많은 강대국으로부터 위협을 받게 된 와칸다. 라몬다, 슈리 그리고 나키아, 오코예, 음바쿠는 각자 사명감을 갖고 와칸다를 지키기 위해 외로운 싸움을 이어간다. 한편, 비브라늄의 패권을 둘러싼 미스터리한 음모와 함께 깊은 해저에서 모습을 드러낸 최강의 적 네이머와 탈로칸의 전사들은 와칸다를 향해 무차별 공격을 퍼붓기 시작하는데…",
              "release_date": "2022-11-09",
              "popularity": 4392.866,
              "vote_average": 7.6,
              "poster_path": "/3PCRWLeqp5y20k6XVzcamZR3BWF.jpg",
              "backdrop_path": "/yYrvN5WFeGYjJnRzhY0QXuo4Isw.jpg",
              "runtime": 162,
              "status": "Released",
              "tagline": "두 세계가 충돌한다",
              "genres": [
                28,
                12,
                878
              ],
              "actors": [
                1083010,
                1267329,
                82104
              ],
              "directors": [
                1056121
              ],
              "keywords": [
                1701,
                9663,
                9715,
                9717,
                179431,
                180059,
                180547,
                195394
              ],
              "videos": [
                "636efa4f9bcd0f00819c2f74",
                "636efa1cf14dad008ddea11f",
                "636efa16ca4f6700bbbf4c6d",
                "636efa2321621b00b49e7a79",
                "636efa292495ab00dc0b9af3",
                "636efa2d9bcd0f00819c2f5a",
                "636efa34ca4f67007fc28ff0",
                "636efa3dfd4f80007fb8617d",
                "634bea9a414291007aa19ad9",
                "62dcde5733a533051fb8cb34"
              ],
              "providers": []
            }
          },
          {
            "model": "movies.movie",
            "pk": 436270,
            "fields": {
              "title": "블랙 아담",
              "original_title": "Black Adam",
              "overview": "기원전 가장 번성하고 위대한 고대 국가였지만 현재는 국제 군사 조직 인터갱의 독재 국가로 전락한 칸다크. 인터갱의 눈을 피해 고대 유물을 찾던 '아드리아나'는 우연히 5000년 동안 잠들어 있던 '블랙 아담'을 깨우게 된다.  엄청난 괴력과 스피드, 방탄 능력과 자유자재의 고공비행, 번개를 쏘는 능력까지. 온몸이 무기인 '블랙 아담'은 자신의 앞을 막아서는 인터갱들을 모조리 쓸어버리고 칸다크 국민들은 이에 열광한다. 한편, 그의 폭주를 막기 위해 호크맨, 닥터 페이트, 아톰 스매셔, 사이클론으로 구성된 히어로 군단 '저스티스 소사이어티'가 칸다크에 나타나는데...",
              "release_date": "2022-10-19",
              "popularity": 3164.736,
              "vote_average": 6.9,
              "poster_path": "/mEdMHGy1FfCUc7PskFO0tibm8jp.jpg",
              "backdrop_path": "/bQXAqRx2Fgc46uCVWgoPz5L5Dtr.jpg",
              "runtime": 125,
              "status": "Released",
              "tagline": "세상을 구할 것인가, 파괴할 것인가?",
              "genres": [
                28,
                14,
                878
              ],
              "actors": [
                18918,
                83860,
                1253353
              ],
              "directors": [
                59521
              ],
              "keywords": [
                952,
                2095,
                9715,
                9717,
                15001,
                155030,
                179431,
                229266
              ],
              "videos": [
                "636efb002495ab008231a174",
                "636efafa8138310077302aa0",
                "636efb0a2495ab008231a179",
                "636efaf49bcd0f007c8c67c5",
                "636efaef2495ab008231a16c",
                "636efb04f14dad008ddea1a8",
                "62dcf78a58361b005468cabf",
                "62a590ea85005d4c07bc1d4c"
              ],
              "providers": []
            }
          },
          {
            "model": "movies.movie",
            "pk": 829280,
            "fields": {
              "title": "에놀라 홈즈 2",
              "original_title": "Enola Holmes 2",
              "overview": "탐정이 된 후 첫 번째 사건을 수임한 에놀라. 하지만 실종된 소녀의 미스터리를 풀기 위해서는 친구들의 도움이 필요하다. 어쩌면 오빠 셜록의 도움까지도.",
              "release_date": "2022-11-04",
              "popularity": 2446.024,
              "vote_average": 7.8,
              "poster_path": "/S6fDnntDjduIWuLW2GcqFasobD.jpg",
              "backdrop_path": "/u9Io1hVnxb2b3T0z99aOK8sq0SN.jpg",
              "runtime": 129,
              "status": "Released",
              "tagline": "",
              "genres": [
                9648,
                12,
                80
              ],
              "actors": [
                1356210,
                73968,
                1558986
              ],
              "directors": [
                173847
              ],
              "keywords": [
                703,
                8250,
                9663,
                160342,
                273879
              ],
              "videos": [
                "632fd8e52a210c007fd16927"
              ],
              "providers": [
                8,
                1796
              ]
            }
          },
          {
            "model": "movies.movie",
            "pk": 532639,
            "fields": {
              "title": "피노키오",
              "original_title": "Pinocchio",
              "overview": "목수 ‘제페토’의 간절한 소원으로 태어난 나무 인형 ‘피노키오’는  진짜 사람이 되기 위해 자신의 양심이 되어줄 귀뚜라미 ‘지미니’와 함께  진실되고 용감한 마음을 가지기로 약속한다.  그러나 거리의 교활한 여우의 꾀임에 넘어간 피노키오는 서커스단에 들어가게 되고, 이기적인 어른들의 욕심으로 철장에 갇혀버리고 만다.  한편, 사라진 피노키오를 찾기 위해 길을 나선 ‘제페토’는 폭우 속에 목숨을 잃을 위기에 처하고 마는데…",
              "release_date": "2022-09-08",
              "popularity": 1010.629,
              "vote_average": 6.7,
              "poster_path": "/aFVjf2zcFzoNgbDKDEHiIw2g1DR.jpg",
              "backdrop_path": "/nnUQqlVZeEGuCRx8SaoCU4XVHJN.jpg",
              "runtime": 105,
              "status": "Released",
              "tagline": "시대를 초월한 명작 ‘피노키오’의 귀환!",
              "genres": [
                14,
                12,
                10751
              ],
              "actors": [
                2382044,
                31,
                24045
              ],
              "directors": [
                24
              ],
              "keywords": [
                2710,
                4344,
                6300,
                209220,
                245230,
                267848,
                302735
              ],
              "videos": [
                "63085c76b7d352007bc9713a",
                "629cafd9d71fb474ded267cc"
              ],
              "providers": [
                337
              ]
            }
          },
          {
            "model": "movies.movie",
            "pk": 616037,
            "fields": {
              "title": "토르: 러브 앤 썬더",
              "original_title": "Thor: Love and Thunder",
              "overview": "이너피스를 위해 자아 찾기 여정을 떠난 천둥의 신 토르. 그러나 우주의 모든 신들을 몰살하려는 신 도살자 고르의 등장으로 토르의 안식년 계획은 산산조각 나 버린다. 토르는새로운 위협에 맞서기 위해 킹 발키리, 코르그, 그리고 전 여자친구 제인과 재회하게 되고, 그녀가 묠니르를 휘두르는 마이티 토르가 되어 나타나 모두를 놀라게 한다. 이제 팀 토르는 고르의 복수에 얽힌 미스터리를 밝히고 더 큰 전쟁을 막기 위한 전 우주적 스케일의 모험을 시작하는데...",
              "release_date": "2022-07-08",
              "popularity": 980.966,
              "vote_average": 6.7,
              "poster_path": "/un8ZDtx2SMwNwXRYy65aItnNjab.jpg",
              "backdrop_path": "/jsoz1HlxczSuTx0mDl2h0lxy36l.jpg",
              "runtime": 119,
              "status": "Released",
              "tagline": "신을 죽이는 자, 신이 상대한다",
              "genres": [
                14,
                28,
                35
              ],
              "actors": [
                74568,
                524,
                3894
              ],
              "directors": [
                55934
              ],
              "keywords": [
                1595,
                1701,
                2036,
                9663,
                9715,
                9717,
                173125,
                179101,
                179430,
                179431,
                180547,
                225679,
                230105,
                262626,
                265839,
                304843
              ],
              "videos": [
                "62dcf7634ccc500068b0fd1c",
                "62dcf7124ccc50004d1c8cd0",
                "62dcf71ee323f3036c0f44a6",
                "62dcf721dc1cb4004fabbd09",
                "62dcf72b27d9cc004f1919b9",
                "62dcf74c4ccc500068b0fd0f",
                "62dcf73527d9cc004f1919bd",
                "62b58e4e1b722c04695f9a3f",
                "62b053173c4344080ae23eb8",
                "628c69f15cea184d122f755e",
                "626542270b5fd60f75748a2c"
              ],
              "providers": [
                337
              ]
            }
          },
          {
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
            }
          },
          {
            "model": "movies.movie",
            "pk": 718930,
            "fields": {
              "title": "불릿 트레인",
              "original_title": "Bullet Train",
              "overview": "운이 없기로 유명한 킬러 레이디버그는 초고속 열차에 탑승해 의문의 서류 가방을 가져오라는 미션을 받는다. 생각보다 쉽게 미션을 클리어한 후 열차에서 내리려는 그를 가로막는 것이 있었으니,  그것은 바로 전세계에서 몰려든 초특급 킬러들. 열차에서 내릴 수 없다면 목숨을 걸고 가방을 지켜야만 한다. 과연 레이디버그는 무사히 열차에서 내려 미션을 완수할 수 있을까?",
              "release_date": "2022-08-24",
              "popularity": 885.009,
              "vote_average": 7.5,
              "poster_path": "/msh4N8dxHk4FeEPZ8VBqHQFQYjI.jpg",
              "backdrop_path": "/zt6sKnx9dEiRCb7oVMlfmmMGJMO.jpg",
              "runtime": 127,
              "status": "Released",
              "tagline": "누구도 멈출 수 없는 논스톱 액션 블록버스터",
              "genres": [
                28,
                35,
                53
              ],
              "actors": [
                287,
                125025,
                27428
              ],
              "directors": [
                40684
              ],
              "keywords": [
                233,
                782,
                818,
                10364,
                13008,
                157904,
                166479,
                179431,
                234041,
                290674
              ],
              "videos": [
                "6302238c5f4b7300826802e3",
                "63022386fb5299007d665005",
                "6302237e7d41aa007e38f077",
                "62cc0b4890b87e1ba092f346",
                "62cc0b0aa9117f0054f1ed1a"
              ],
              "providers": []
            }
          },
          {
            "model": "movies.movie",
            "pk": 766507,
            "fields": {
              "title": "프레이",
              "original_title": "Prey",
              "overview": "300년 전 아메리카, 용맹한 전사를 꿈꾸는 원주민 소녀 나루는 갑작스러운 곰의 습격으로 절체절명의 위기에 놓인 순간, 정체를 알 수 없는 외계 포식자 프레데터를 목격하게 된다.  자신보다 강한 상대를 향한 무자비한 사냥을 시작한 프레데터. 최첨단 기술과 무기로 진화된 외계 포식자 프레데터의 위협이 점점 다가오고 나루는 부족을 지키기 위해 자신만의 기지와 무기로 생존을 건 사투를 시작하는데…",
              "release_date": "2022-08-05",
              "popularity": 817.303,
              "vote_average": 7.9,
              "poster_path": "/eicYAopFKOL3orcNTJZ4TGtZQQ1.jpg",
              "backdrop_path": "/7ZO9yoEU2fAHKhmJWfAc2QIPWJg.jpg",
              "runtime": 100,
              "status": "Released",
              "tagline": "하나만 살아남는다",
              "genres": [
                53,
                28,
                878
              ],
              "actors": [
                1654001,
                3675371,
                87126
              ],
              "directors": [
                568322
              ],
              "keywords": [
                414,
                4862,
                9675,
                9951,
                10322,
                10468,
                11181,
                15162,
                157513,
                158175,
                179419,
                186497,
                215162,
                269485,
                287699,
                298551,
                301974
              ],
              "videos": [
                "62edcfc1ae281100915f3131",
                "62edcfc91c6329007c7b605f",
                "62edcfd046aed400917de011",
                "62edcfdc706e56007a16db12",
                "62bee8b2af6e94046b3e5240"
              ],
              "providers": [
                337
              ]
            }
          },
          {
            "model": "movies.movie",
            "pk": 507086,
            "fields": {
              "title": "쥬라기 월드: 도미니언",
              "original_title": "Jurassic World Dominion",
              "overview": "공룡들의 터전이었던 이슬라 누블라 섬이 파괴된 후,  마침내 공룡들은 섬을 벗어나 세상 밖으로 출몰한다. 지상에 함께 존재해선 안 될 위협적 생명체인 공룡의 등장으로 인류 역사상 겪어보지 못한 사상 최악의 위기를 맞이한 인간들. 지구의 최상위 포식자 자리를 걸고 인간과 공룡의 최후의 사투가 펼쳐진다.",
              "release_date": "2022-06-01",
              "popularity": 803.21,
              "vote_average": 7,
              "poster_path": "/odxdUZWZ7fBfy3ZRj063wuJnZvo.jpg",
              "backdrop_path": "/3PieOs1t6dPHWlgvX3XoqTIQLqN.jpg",
              "runtime": 147,
              "status": "Released",
              "tagline": "이제 모든 것이 끝난다, 지상 최대 블록버스터의 압도적 피날레!",
              "genres": [
                12,
                28,
                878
              ],
              "actors": [
                73457,
                18997,
                4784
              ],
              "directors": [
                930707
              ],
              "keywords": [
                11100,
                12616,
                170865,
                197063,
                242578
              ],
              "videos": [
                "6205d069848eb90067fa5b7a"
              ],
              "providers": []
            }
          },],
      }
    },
    methods: {
      goDetail(id) {
        this.$router.push({ name: 'MovieDetail', params: { movie_id: id }, query: {movie_id: id}})
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import './MyPageRatingSwiper.scss';
</style>