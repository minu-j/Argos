<template>
  <div>
    <div>
      <div>
        팔로워 {{ followData.follower_count }}
        <div>
          {{followData.followers}}
        </div>
      </div>
      <div>
        팔로잉 {{ followData.following_count }}
        <div>
          {{followData.followings}}
        </div>
      </div>
    </div>
    <div v-if="!isUser">
      <span v-if="isFollow">
        <span>생각해보니 안맞는 것 같으신가요?</span>
        <span class="heart" @click="followUser">팔로우 취소</span>
      </span>
      <span v-else>
        <span>이 회원과 취향이 비슷하신가요?</span>
        <span class="heart" @click="followUser">팔로우</span>
      </span>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UserFollow',
  data() {
    return {
      isUser: false,
      userName: null,
      isFollow: null,
      followData: {}
    }
  },
  methods:{
    followUser() {
      const Token = this.$store.state.token

      axios({
          method: 'post',
          url: `${API_URL}/accounts/follow/${this.userName}/`,
          headers: {
            Authorization: `Token ${Token}`
          }
        })
        .then(res => {
          console.log(res)
          if (this.isFollow) {
            this.followData.follower_count--
            this.isFollow = !this.isFollow
          } else {
            this.followData.follower_count++
            this.isFollow = !this.isFollow
          }
        })
        .catch(err => {

          console.log(err)
        })
    },
  },
  mounted() {
    this.userName = window.location.pathname.replaceAll('/mypage/', '')
    const Token = this.$store.state.token

    axios({
        method: 'get',
        url: `${API_URL}/accounts/follow/list/${this.userName}/`,
        headers: {
          Authorization: `Token ${Token}`
        }
      })
      .then(res => {
        console.log(res.data)
        this.followData = res.data["0"]
      })
      .catch(err => {

        console.log(err)
      })
      
    if (this.userName == this.$store.state.username) {
      this.isUser = true
    } else {
      const Token = this.$store.state.token

      axios({
          method: 'get',
          url: `${API_URL}/accounts/follow/${this.userName}/`,
          headers: {
            Authorization: `Token ${Token}`
          }
        })
        .then(res => {
          this.isFollow = res.data.isFollow
        })
        .catch(err => {

          console.log(err)
        })
    }
  }
}
</script>

<style scoped>

</style>