<template>
  <!-- 회원 탈퇴하기 -->
  <div class="out" @click="onSignout">회원 탈퇴하기</div>
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
}

</script>

<style>

</style>