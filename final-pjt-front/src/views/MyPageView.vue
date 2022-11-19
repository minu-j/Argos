<template>
  <div>
    <h1>mypage</h1>
    {{userInfo}}
    <p></p>
  </div>
</template>

<script>
export default {
  name: 'MyPageView',
  computed: {
    userInfo() {
      return this.$store.state.username
    }
  }
}
</script>

<style lang="scss">
@import "./MyPageView.scss";
</style>