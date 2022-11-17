<template>
  <div>
    <h1>Detail</h1>
    <h3>{{ movie }}</h3>
  </div>
</template>

<script>
export default {
  name: 'MovieDetail',
  props: {
    movie: Object,
  }
}
</script>

<style lang="scss" scoped>
  @import './MovieDetail.scss';
</style>