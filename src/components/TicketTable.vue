<template>
  <div class="timetable">
    <div v-if="isSelected" class="timetable-container">
      <p>아래 내용은 더미데이터입니다.</p>
      <div
        class="timetable-movie"
        v-for="(movie, index) in timeTable"
        :key="`movie-${index}`"
      >
        <span class="timetable-movie-title">{{ movie.title }}</span>
        <span class="timetable-movie-age">{{ movie.rating }}</span>
        <div
          class="timetable-movie-theater"
          v-for="(theater, index) in movie.theater"
          :key="`theater-${index}`"
        >
          {{ theater.num }}
          <div class="timetable-movie-theater-schedule">
            <div
              class="timetable-movie-theater-time"
              v-for="(schedule, index) in theater.schedule"
              :key="`schedule-${index}`"
            >
              <a :href="schedule.link" target="_blank">
                {{ schedule.time }}
              </a>
            </div>
          </div>
        </div>
        <hr />
      </div>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
// import cheerio from "cheerio";

export default {
  name: "TicketTable",
  props: {
    selectedTheater: Object,
  },
  data() {
    return {
      isSelected: false,
      timeTable: [],
    };
  },
  watch: {
    selectedTheater: function () {
      this.isSelected = true;
      this.getTimeTable();
    },
  },
  methods: {
    getTimeTable() {
      this.timeTable = [
        {
          title: "소울메이트",
          rating: "12세 관람가",
          theater: [
            {
              num: "(1관)",
              schedule: [
                {
                  time: "23:20",
                  link: "http://www.cgv.co.kr/ticket/?MOVIE_CD=20032165&MOVIE_CD_GROUP=20032165&PLAY_YMD=20230320&THEATER_CD=0293&PLAY_START_TM=2320&AREA_CD=04&SCREEN_CD=001&utm_source=naver&utm_medium=CP&utm_campaign=NAVER",
                },
              ],
            },
            {
              num: "(8관)",
              schedule: [
                {
                  time: "22:10",
                  link: "http://www.cgv.co.kr/ticket/?MOVIE_CD=20032165&MOVIE_CD_GROUP=20032165&PLAY_YMD=20230320&THEATER_CD=0293&PLAY_START_TM=2210&AREA_CD=04&SCREEN_CD=008&utm_source=naver&utm_medium=CP&utm_campaign=NAVER",
                },
              ],
            },
          ],
        },
        {
          title: "스즈메의 문단속",
          rating: "12세 관람가",
          theater: [
            {
              num: "(10관)",
              schedule: [
                {
                  time: "23:00",
                  link: "http://www.cgv.co.kr/ticket/?MOVIE_CD=20031945&MOVIE_CD_GROUP=20031945&PLAY_YMD=20230320&THEATER_CD=0293&PLAY_START_TM=2300&AREA_CD=04&SCREEN_CD=010&utm_source=naver&utm_medium=CP&utm_campaign=NAVER",
                },
              ],
            },
          ],
        },
        {
          title: "샤잠! 신들의 분노",
          rating: "12세 관람가",
          theater: [
            {
              num: "(9관)",
              schedule: [
                {
                  time: "22:50",
                  link: "http://www.cgv.co.kr/ticket/?MOVIE_CD=20031990&MOVIE_CD_GROUP=20031990&PLAY_YMD=20230320&THEATER_CD=0293&PLAY_START_TM=2250&AREA_CD=04&SCREEN_CD=009&utm_source=naver&utm_medium=CP&utm_campaign=NAVER",
                },
              ],
            },
          ],
        },
        {
          title: "더 퍼스트 슬램덩크",
          rating: "12세 관람가",
          theater: [
            {
              num: "(씨네앤포레)",
              schedule: [
                {
                  time: "23:30",
                  link: "http://www.cgv.co.kr/ticket/?MOVIE_CD=20031675&MOVIE_CD_GROUP=20031612&PLAY_YMD=20230320&THEATER_CD=0293&PLAY_START_TM=2330&AREA_CD=04&SCREEN_CD=006&utm_source=naver&utm_medium=CP&utm_campaign=NAVER",
                },
              ],
            },
          ],
        },
        {
          title: "귀멸의 칼날: 상현집결, 그리고 도공 마을로",
          rating: "15세 관람가",
          theater: [
            {
              num: "(7관)",
              schedule: [
                {
                  time: "22:20",
                  link: "http://www.cgv.co.kr/ticket/?MOVIE_CD=20031992&MOVIE_CD_GROUP=20031992&PLAY_YMD=20230320&THEATER_CD=0293&PLAY_START_TM=2220&AREA_CD=04&SCREEN_CD=007&utm_source=naver&utm_medium=CP&utm_campaign=NAVER",
                },
              ],
            },
          ],
        },
      ];
      // const url = `/search.naver?query=${this.selectedTheater.place_name}영화시간표`;

      // axios
      //   .get(url)
      //   .then((response) => {
      //     this.timeTable = [];
      //     const $ = cheerio.load(response.data);
      //     $("tbody._wrap_time_table > tr").map((i, element) => {
      //       const movie = {
      //         title: null,
      //         rating: null,
      //         theater: [],
      //       };
      //       movie.rating = $(element).find("th > span").text();
      //       movie.title = $(element).find("th > a").text();
      //       $(element)
      //         .find("td > div")
      //         .map((i, element) => {
      //           const theater = {
      //             num: null,
      //             schedule: [],
      //           };
      //           theater.num = $(element).find("span.place").html();

      //           $(element)
      //             .find("span.time_info > a")
      //             .map((i, element) => {
      //               const schedule = {
      //                 time: null,
      //                 link: null,
      //               };
      //               schedule.time = $(element).text();
      //               schedule.link = $(element)[0]["attribs"]["href"];
      //               theater.schedule.push(schedule);
      //             });
      //           movie.theater.push(theater);
      //         });
      //       this.timeTable.push(movie);
      //     });
      //   })
      //   .catch((error) => {
      //     console.log("데이터 수신 실패", error);
      //   });
    },
  },
};
</script>

<style lang="scss" scoped>
@import "./TicketTable.scss";
</style>
