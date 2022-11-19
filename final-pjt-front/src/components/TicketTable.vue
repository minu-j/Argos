<template>
  <div class="timetable">
    <div v-if="isSelected" class="timetable-container">
      <div class="timetable-movie" v-for="(movie, index) in timeTable" :key="`movie-${index}`">
        <span class="timetable-movie-title">{{ movie.title }}</span>
        <span class="timetable-movie-age">{{ movie.rating }}</span>
        <div class="timetable-movie-theater" v-for="(theater, index) in movie.theater" :key="`theater-${index}`">
          {{theater.num}}
          <div class="timetable-movie-theater-schedule">
            <div class="timetable-movie-theater-time" v-for="(schedule, index) in theater.schedule" :key="`schedule-${index}`">
              <a :href="schedule.link" target="_blank">
                {{ schedule.time }}
              </a>
            </div>
          </div>
        </div>
        <hr>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import cheerio from 'cheerio'

export default {
  name: 'TicketTable',
  props: {
    selectedTheater: Object,
  },
  data() {
    return {
      isSelected: false,
      timeTable: [],
    }
  },
  watch: {
    selectedTheater: function() {
      this.isSelected = true
      this.getTimeTable()
    }
  },
  methods: {
    getTimeTable() {
      const url = `/search.naver?query=${this.selectedTheater.place_name}영화시간표`

      axios.get(url)
        .then((response) => {
          this.timeTable = []
          const $ = cheerio.load(response.data)
          $('tbody._wrap_time_table > tr').map((i, element) => {
            const movie = {
              title: null, 
              rating: null,
              theater: []
            }
            movie.rating = $(element).find('th > span').text()
            movie.title = $(element).find('th > a').text()
            $(element).find('td > div').map((i, element) => {
              const theater = {
                num: null,
                schedule: []
              }
              theater.num = $(element).find('span.place').html()

              $(element).find('span.time_info > a').map((i, element) => {
                const schedule = {
                  time: null,
                  link: null
                }
                schedule.time = $(element).text()
                schedule.link = $(element)[0]['attribs']['href']
                theater.schedule.push(schedule)
              })
              movie.theater.push(theater)
            })
            this.timeTable.push(movie)
          })
        })
        .catch((error) => {
          console.log('데이터 수신 실패', error)
        })
    }
  }
}
</script>

<style lang="scss" scoped>
  @import './TicketTable.scss';
</style>