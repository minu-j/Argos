<template>
  <div id="play">
    <div id="logo">
      <img src="@/assets/ARGOS_logo.svg" alt="">
      <div id="logo-play">PLAY</div>
    </div>
    <div v-for="(playList, index) in playData" :key="`playlist-${index}`">
      <play-swiper id="play-swiper" :play-list="playList"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import PlaySwiper from '../components/PlaySwiper.vue'

export default {
  components: { PlaySwiper },
  name: 'PlayView',
  data() {
    return {
      playData: {}
    }
  },
  mounted() {
    const API_URL = this.$store.state.API_URL
    console.log(API_URL)
    const Token = this.$store.state.token
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/play/`,
      headers: {
        Authorization: `Token ${Token}`
      },
    })
      .then(res => {
        this.playData = res.data
      })
      .catch(err => {
        console.log(err)
      })

  }
}
</script>

<style lang="scss" scoped>
@import "@/views/PlayView.scss";
</style>