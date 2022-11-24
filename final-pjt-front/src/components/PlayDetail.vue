<template>
  <div>
    <div>
      <iframe 
        width="840" 
        height="360" 
        :src="`https://www.youtube-nocookie.com/embed/${videoKey}?showinfo=0&modestbranding=1&rel=0&autoplay=1&fs=1`" 
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
      >
      </iframe>
    </div>
    <div id="bg"></div>
  </div>
</template>

<script>
export default {
  name: 'PlayDetail',
  data() {
    return {
      videoKey: null
    }
  },
  mounted() {
    this.videoKey = window.location.pathname.replaceAll('/play/', '')
  }
}
</script>

<style lang="scss" scoped>
  @import './PlayDetail.scss';
</style>