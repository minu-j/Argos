<template>
  <div id="app">
    <nav id="navbar" class="navbar navbar-expand-md navbar-dark">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand" id="logo" href="">
          <img id="logo-img" src="@/assets/ARGOS_logo.svg" alt="LOGO">
          <span>ARGOS</span>
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <div class="nav-item--select">
                <div class="nav-item--select-bg"></div>
              </div>
              <router-link to="/ticket">Ticket</router-link>
            </li>
            <li class="nav-item">
              <div class="nav-item--select">
                <div class="nav-item--select-bg"></div>
              </div>
              <router-link to="/play">Play</router-link>
            </li>
            <li class="nav-item">
              <div class="nav-item--select">
                <div class="nav-item--select-bg"></div>
              </div>
              <router-link to="/news">News</router-link>
            </li>
          </ul>
          <ul class="navbar-nav">
            <li class="nav-item">
              <div class="nav-item--select">
                <div class="nav-item--select-bg"></div>
              </div>
              <!-- 임시 로그인/ 로그아웃 -->
              <router-link v-if="!isLogin" id="nav-menu" :to="{ name: 'LoginView' }">Login</router-link>
              <button v-else @click="logOut">LogOut</button>              
            </li>
            <li class="nav-item nav-item--rightside">
              <div class="nav-item--select">
                <div class="nav-item--select-bg"></div>
              </div>
              <router-link to="/mypage">My Page</router-link>
            </li>
            <!-- 임시 회원가입 -->
            <router-link v-if="!isLogin" id="nav-menu" :to="{ name: 'SignUpView' }">SignUp</router-link>

           
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
    },
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
  }
}
</script>

<style lang="scss" scoped>
@import "@/style/reset.scss";
@import "@/App.scss";
</style>

