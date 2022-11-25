<template>
  <div>
    <div class="auth">
      <h1 class="auth-title">LOGIN</h1>
      <form class="auth-form" @submit.prevent="logIn">
        <input @keyup.enter="logIn" class="auth-form-input" placeholder="Username" type="text" id="username" v-model="username">
        <div class="auth-password">
          <img @mouseup="passwordShowTogle" class="password-show" v-if="passwordShow" src="@/assets/eye.png" alt="">
          <img @mousedown="passwordShowTogle" class="password-show" v-else src="@/assets/hidden.png" alt="">
          <input @keyup.enter="logIn" class="auth-form-input" placeholder="Password" type="password" id="password" v-model="password">
        </div>
        <div class="check-word" v-if="failedLogin === true">
          <span class="info-red">입력 정보를 다시 확인해주세요.</span>
        </div>
        <div @click="logIn" class="auth-form-submit">Press Enter</div>
        <div @click="moveToSignup" class="auth-form-move">아직 회원이 아니신가요?</div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
      passwordShow: false,
      failedLogin: false
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then(res => {
          const payload = {
            token: res.data.key,
            isFirst: false
          }
          this.$store.commit('SAVE_TOKEN', payload)

          axios({
            method: 'get',
            url: `${API_URL}/accounts/user/`,
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            }
          })
            .then(res => {
              const payload = {
                userId: res.data.pk,
                username: res.data.username
              }
              console.log(payload)
              this.$store.commit('SAVE_USER_DATA', payload)
              })
            .then(() =>{
              this.$router.push({ name:'HomeView' })
            })
            .catch(err => {
              console.log(err)
            })

        })
        .catch(err => {
          console.log(err)
          this.failedLogin = true
        })
    },
    logOut() {
      this.$store.dispatch('logout')
    },
    moveToSignup() {
      this.$router.push({name: 'SignUpView'})
    },
    passwordShowTogle() {
      
      const passwordInput = document.querySelector('#password')
      if (this.passwordShow) {
        passwordInput.removeAttribute('type')
        passwordInput.setAttribute('type', 'password')
        this.passwordShow = !this.passwordShow
      } else {
        passwordInput.removeAttribute('type')
        passwordInput.setAttribute('type', 'text')
        this.passwordShow = !this.passwordShow
      }
      
    }
  }
}
</script>
<style lang="scss" scoped>
@import "./AuthForm.scss";
</style>