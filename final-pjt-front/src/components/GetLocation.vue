<template>
  <div>
  </div>
</template>

<script>
export default {
  name: 'GetLocation',
  methods: {
  },
  mounted() {
    // 접속시 사용자 위치정보 요청
    navigator.geolocation.getCurrentPosition((position) => {
      const payload = {
        latitude: position.coords.latitude,
        longitude: position.coords.longitude
      }
      this.$store.commit('GET_LOCATION', payload)
    })
  }
}
</script>

<style>

</style>