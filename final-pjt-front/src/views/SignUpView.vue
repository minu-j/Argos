<template>
  <div>
    <div class="auth">
      <h1 class="auth-title">SIGNUP</h1>
      <form class="auth-form" @submit.prevent="signUp">
        <input @keyup="checkKorean" class="auth-form-input" placeholder="Username" type="text" id="username" v-model="username">
        <div class="check-word">
          <div id="info-gray">영문 대소문자, 숫자만 입력 가능합니다.</div>
          <div v-if="usernameReduplication === true" id="info-red">✗ 이미 사용중인 이름입니다.</div>
          <div v-if="usernameReduplication === false" id="info-green">✓ 사용할 수 있는 이름입니다.</div>
        </div>
        <div v-if="username && usernameReduplication === false" class="auth-password">
          <img @mouseup="passwordShowTogle" class="password-show" v-if="passwordShow" src="@/assets/eye.png" alt="">
          <img @mousedown="passwordShowTogle" class="password-show" v-else src="@/assets/hidden.png" alt="">
          <input @keyup="checkPassword" class="auth-form-input" placeholder="Password" type="password" id="password1" v-model="password1" onkeyup="">
        </div>
        <!-- 비밀번호1 검증 안내 -->
        <div v-if="password1 && usernameReduplication === false" class="check-word">
          <div v-if="checkPasswordData.common === 'fail'" id="info-red">✗ 일반적인 비밀번호가 아니어야 합니다.</div>
          <div v-else id="info-green">✓ 일반적인 비밀번호가 아닙니다.</div>
          <div v-if="checkPasswordData.similarity === 'fail'" id="info-red">✗ Username과 유사하지 않아야 합니다.</div>
          <div v-else id="info-green">✓ Username과 유사하지 않습니다.</div>
          <div v-if="checkPasswordData.min_length === 'fail'" id="info-red">✗ 8글자 이상이어야 합니다.</div>
          <div v-else id="info-green">✓ 8글자 이상입니다.</div>
          <div v-if="checkPasswordData.symbols === 'fail'" id="info-red">✗ 영문, 숫자, 특수문자가 포함되어야 합니다.</div>
          <div v-else id="info-green">✓ 영문, 숫자, 특수문자를 모두 포함합니다.</div>
        </div>
        <!-- 위 1차 검증을 모두 통과해야 2번째 비밀번호 입력 창 띄우기 -->
        <div v-if="allPass && usernameReduplication === false" class="auth-password">
          <img @mouseup="passwordShowTogle" class="password-show" v-if="passwordShow" src="@/assets/eye.png" alt="">
          <img @mousedown="passwordShowTogle" class="password-show" v-else src="@/assets/hidden.png" alt="">
          <input @keyup.enter="signUp" @keyup="checkSame" class="auth-form-input" placeholder="Password confirm" type="password" id="password2"  v-model="password2">
        </div>
        <!-- 비밀번호2 동일한지 안내 -->
        <div v-if="password2 && isPasswordSame !== null && usernameReduplication === false" class="check-word">
          <div v-if=" isPasswordSame" id="info-green">✓ 비밀번호가 동일합니다.</div>
          <div v-else id="info-red">✗ 비밀번호가 같지 않습니다.</div>
        </div>
        <div v-if="allPass && isPasswordSame && usernameReduplication === false" @click="signUp" class="auth-form-submit">Press Enter</div>
        <div @click="moveToLogin" class="auth-form-move">이미 회원이신가요?</div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2:  null,
      passwordShow: false,
      checkPasswordData: {
        common: 'fail',
        similarity: 'fail',
        min_length: 'fail',
        symbols: 'fail'
      },
      allPass: false,
      isPasswordSame: null,
      usernameReduplication: null
    }
    
  },
  watch: {
    // 비밀번호 체크해서 하나라도 fail이면 allPass = false
    checkPasswordData: function () {
     if (this.checkPasswordData.common === 'pass' && this.checkPasswordData.similarity === 'pass' && this.checkPasswordData.min_length === 'pass' && this.checkPasswordData.symbols === 'pass') {
      this.allPass = true
     } else {
      this.allPass = false
     }

    }
  },
  methods: {
    // 회원가입
    signUp() {
      if (this.allPass && this.isPasswordSame) {
        const username = this.username
        const password1 = this.password1
        const password2 = this.password2
  
        const payload = {
          username: username,
          password1: password1,
          password2: password2,
        }
        this.$store.dispatch('signUp', payload)

      }
    },
    // 로그인 이동
    moveToLogin() {
      this.$router.push({name: 'LoginView'})
    },
    // 비밀번호 보여줄지 가릴지 토글
    passwordShowTogle() {
      const passwordInput1 = document.querySelector('#password1')
      const passwordInput2 = document.querySelector('#password2')
      if (this.passwordShow) {
        passwordInput1.removeAttribute('type')
        passwordInput1.setAttribute('type', 'password')
        passwordInput2.removeAttribute('type')
        passwordInput2.setAttribute('type', 'password')
        this.passwordShow = !this.passwordShow
      } else {
        passwordInput1.removeAttribute('type')
        passwordInput1.setAttribute('type', 'text')
        passwordInput2.removeAttribute('type')
        passwordInput2.setAttribute('type', 'text')
        this.passwordShow = !this.passwordShow
      } 
    },
    // 실시간 비밀번호 검증
    checkPassword() {
      this.checkSame()
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'post',
        url: `${API_URL}/accounts/passwordprecheck/`,
        data: {
          username: this.username,
          password1: this.password1
        }
      })
        .then((res) =>{
          this.checkPasswordData = res.data
        })
        .catch((err) =>{
          console.log(err)
        })
    },
    // 비밀번호 확인이 동일한지 검증
    checkSame() {
      console.log(this.password1, this.password2)
      if (this.password1 === this.password2) {
        this.isPasswordSame = true
      } else {
        this.isPasswordSame = false
      }
      console.log(this.isPasswordSame)
    },
    // username 한글입력 막기
    checkKorean() {
      const usernameInput = document.querySelector('#username')
      usernameInput.value = usernameInput.value.replace(/[^A-Za-z0-9]/ig, '')
      
      // 이후 username 사용 가능 검증
      if (usernameInput.value) {
        const API_URL = 'http://127.0.0.1:8000'
        axios({
          method: 'get',
          url: `${API_URL}/accounts/usernameprecheck/${usernameInput.value}/`,
          })
          .then((res) =>{
            if (res.data.data === 'pass') {
              this.usernameReduplication = false
            } else {
              this.usernameReduplication = true
            }
          })
          .catch((err) =>{
            console.log(err)
          })
      } else {
        this.usernameReduplication = null
      }
    }
  }
}
</script>
<style lang="scss" scoped>
@import "./AuthForm.scss";
</style>