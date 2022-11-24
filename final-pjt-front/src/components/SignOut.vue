<template>
  <!-- 회원 탈퇴하기 -->
  <div class="out" @click="onSignout" v-if="isMypage">회원 탈퇴</div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name : "SignOut",
  methods: {
    ...mapActions(['signout']),
    onSignout() {
        this.signout()
    },
  },
  computed: {
    isMypage() {
      const pageName = window.location.pathname.replaceAll('/mypage/', '')
      const myName = this.$store.state.username
      if (pageName === myName) {
        return true
      } else {
        return false
      }
    }
  }
}

</script>

<style lang="scss" scoped>
  @import './SignOut.scss';
</style>