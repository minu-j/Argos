<template>
  <div>
    <div class="follow-people">
      <div class="follow-people-box">
        <div class="follow-people-box-title">팔로워</div>
        <div class="follow-people-box-count">{{ followData.follower_count }}명</div>
        <div class="follow-people-box-list">
          <span class="follow-people-box-list-item" @click="goProfile(follower.username)" v-for="(follower, index) in followData.followers" :key="`follower-${index}`">{{follower.username}}</span>
        </div>
      </div>
      <div class="follow-people-box">
        <div class="follow-people-box-title">팔로잉</div>
        <div class="follow-people-box-count">{{ followData.following_count }}명</div>
        <div class="follow-people-box-list">
          <span class="follow-people-box-list-item" @click="goProfile(following.username)" v-for="(following, index) in followData.followings" :key="`follower-${index}`">{{following.username}}</span>
        </div>
      </div>
    </div>
    <div class="follow-user" v-if="!isUser">
      <span v-if="isFollow">
        <span class="follow-user-title">생각해보니 안맞는 것 같으신가요?</span>
        <span class="follow-user-btn" @click="followUser">팔로우 취소</span>
      </span>
      <span v-else>
        <span class="follow-user-title">이 회원님과 취향이 비슷하신가요?</span>
        <span class="follow-user-btn" @click="followUser">팔로우</span>
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
    // 팔로우 데이터 불러오기
    getFollow() {
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
    },
    // 이 유저 팔로우/취소하기
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
          this.getFollow()
        })
        .catch(err => {

          console.log(err)
        })
    },
    goProfile(username) {
      console.log(username)
      this.$router.push(`/mypage/${username}`)
      this.$router.go(this.$router.currentRoute)
    }
  },
  mounted() {
    this.getFollow()
  }
}
</script>

<style lang="scss" scoped>
  @import './UserFollow.scss';
</style>