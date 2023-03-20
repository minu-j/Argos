<template>
  <div>
    <div @click="goHome" id="start-cover">
      <div id="video-box">
        <video muted autoplay loop src="@/assets/VintageCinemaFilmLoop.mp4" type="video/mp4"></video>
        <div>클릭하여 시작하기</div>
      </div>
      <div>
      </div>
      <div id="bg"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StartView',
  methods: {
    goHome() {
      this.$router.push('/home')
    }
  },
  mounted() {
    const docStyle = document.documentElement.style;
    document.addEventListener('mousemove', function(e) {
      docStyle.setProperty('--mouse-x', e.clientX);
      docStyle.setProperty('--mouse-y', e.clientY);
    });
  }
}
</script>

<style lang="scss" scoped>
@import "@/views/StartView.scss";
</style>