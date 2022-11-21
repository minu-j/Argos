<template>
  <span>
    <span class="heart-btn" v-if="isUser">
      <span class="content" @click="heart">
        <span class="heart" @click="follow"></span>
      </span>
    </span>
  </span>
</template>

<script>
// import jwt_decode from "jwt-decode";  -> 헤더에 토큰 담아 보내는 거
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'userFollow',
  data: function () {
    return {
      // isActive:'heart-active',
      isUser: null,
    }
  },
  methods:{
    setToken: function () {
      const config = {
        Authorization: `Token ${this.$store.state.token}`
      }
      return config
    },
    follow: function () {
      axios({
          method: 'post',
          url: `${API_URL}/accounts/follow/${this.$route.params.username}/`,
          headers: this.setToken()
        })
        .then(res => {
          this.$emit('count',res.data.count)
        })
        .catch(err => {

          console.log(err)
        })
    }, 
  },
}
</script>

<style scoped>

</style>