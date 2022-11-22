<template>
  <div>
    <div class="auth">
      <h1 class="auth-title">SIGNUP</h1>
      <form class="auth-form" @submit.prevent="signUp">
        <input @keyup.enter="signUp" class="auth-form-input" placeholder="Username" type="text" id="username" v-model="username"><br>
        <input @keyup.enter="signUp" class="auth-form-input" placeholder="Password" type="password" id="password1" v-model="password1"><br>
        <input @keyup.enter="signUp" class="auth-form-input" placeholder="Password confirm" type="password" id="password2"  v-model="password2">
        <div @click="signUp" class="auth-form-submit">Press enter</div>
        <div @click="moveToLogin" class="auth-form-move">이미 회원이신가요?</div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2:  null,
    }
    
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      }
      this.$store.dispatch('signUp', payload)
    },
    moveToLogin() {
      this.$router.push({name: 'LoginView'})
    }
  }
}
</script>
<style lang="scss" scoped>
@import "./AuthForm.scss";
</style>