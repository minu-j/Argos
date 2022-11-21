<template>
  <div id="app">
    <nav id="navbar" class="navbar navbar-expand-md navbar-dark">
      <div class="container-fluid">
        <a @click="reLoad" class="navbar-brand" id="logo" href="">
          <img id="logo-img" src="@/assets/ARGOS_logo.svg" alt="LOGO">
          <span>ARGOS</span>
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <div class="nav-item--select">
                <div class="nav-item--select-bg"></div>
              </div>
              <router-link to="/ticket">TICKET</router-link>
            </li>
            <li class="nav-item">
              <div class="nav-item--select">
                <div class="nav-item--select-bg"></div>
              </div>
              <router-link to="/play">PLAY</router-link>
            </li>
            <li class="nav-item">
              <div class="nav-item--select">
                <div class="nav-item--select-bg"></div>
              </div>
              <router-link to="/news">NEWS</router-link>
            </li>
          </ul>
          <ul class="navbar-nav">
            <!-- 로그인 되어있을 때 오른쪽 nav -->
            <li v-if="isLogin" class="nav-item nav-item--rightside">
              <div class="nav-item--select">
                <div class="nav-item--select-bg"></div>
              </div>
              <router-link to="/mypage">MYPAGE</router-link>
            </li>
            <li v-if="isLogin" class="nav-item nav-item--rightside">
              <div class="nav-item--select">
                <div class="nav-item--select-bg"></div>
              </div>
              <a @click="logOut">LOGOUT</a>
            </li>
            <!-- 로그인 안되어있을 때 오른쪽 nav -->
            <li v-if="!isLogin" class="nav-item nav-item--rightside">
              <div class="nav-item--select">
                <div class="nav-item--select-bg"></div>
              </div>
              <router-link v-if="!isLogin" id="nav-menu" :to="{ name: 'SignUpView' }">SIGNUP</router-link>
            </li>
            <li v-if="!isLogin" class="nav-item nav-item--rightside">
              <div class="nav-item--select">
                <div class="nav-item--select-bg"></div>
              </div>
              <router-link v-if="!isLogin" id="nav-menu" :to="{ name: 'LoginView' }">LOGIN</router-link>
            </li>

            <!-- 임시 회원가입 -->

          </ul>
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>


<script>
export default {
  
  methods: {
    logOut() {
      this.$store.commit('NULL_TOKEN')
      alert('로그아웃 되었습니다.')
      this.$router.push({ name:'HomeView' })
      this.$router.go(this.$router.currentRoute)
    },
    // signOut() {
    //     this.$store.commit('DELETE_TOKEN')
    //     alert('성공적으로 회원탈퇴 처리되었습니다.')
    //     this.$router.push({ name:'HomeView' })
    // },
    reLoad() {
      this.$router.push({ name:'HomeView' })
      this.$router.go(this.$router.currentRoute)
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  created() {
    this.$store.dispatch('getBoxoffice')
  }
}
</script>

<style lang="scss">
@import "@/style/reset.scss";
@import "@/App.scss";
</style>

