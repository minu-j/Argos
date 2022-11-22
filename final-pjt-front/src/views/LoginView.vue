<template>
  <div>
    <div class="auth">
      <h1 class="auth-title">LOGIN</h1>
      <form class="auth-form" @submit.prevent="logIn">
        <input @keyup.enter="logIn" class="auth-form-input" placeholder="Username" type="text" id="username" v-model="username"><br>
        <div class="auth-password" @click="passwordShowTogle">
          <img class="password-show" v-if="passwordShow" src="@/assets/eye.png" alt="">
          <img class="password-show" v-else src="@/assets/hidden.png" alt="">
          <input @keyup.enter="logIn" class="auth-form-input" placeholder="Password" type="password" id="password" v-model="password"><br>
        </div>
        <div @click="logIn" class="auth-form-submit">Press enter</div>
        <div @click="moveToSignup" class="auth-form-move">아직 회원이 아니신가요?</div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
      passwordShow: false
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username,
        password
      }
      this.$store.dispatch('logIn', payload)
    },
    logOut() {
      this.$store.dispatch('logout')
    },
    moveToSignup() {
      this.$router.push({name: 'SignUpView'})
    },
    passwordShowTogle() {
      this.passwordShow = !this.passwordShow
    }
  }
}
</script>
<style lang="scss" scoped>
@import "./AuthForm.scss";
</style>