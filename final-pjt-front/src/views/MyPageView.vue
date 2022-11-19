<template>
  <div>
    <h1>mypage</h1>
    {{userInfo}}
    <p></p>
    <!-- <router-link to="/userFollow">follow</router-link> -->
  </div>
</template>

<script>
// import UserFollow from '@/components/UserFollow.vue'

export default {
  name: 'MyPageView',
  // components: { 
  //   UserFollow,
  // },
  computed: {
    userInfo() {
      return this.$store.state.username
    },
  }
}
</script>

<style lang="scss">
@import "./MyPageView.scss";
</style>