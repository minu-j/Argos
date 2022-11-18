<template>
  <div id="theater">
    <div v-if="isSelected" id="theater-info">
      <div>
        <span id="theater-info-title">{{ selectedTheater.place_name }}</span>
        <span id="theater-info-distance">{{ selectedTheater.distance / 1000 }}km</span>
      </div>
      <a :href="`${selectedTheater.place_url}`" class="theater-discription">{{ selectedTheater.road_address_name }}</a>
      <a href="tel:" class="theater-discription">{{ selectedTheater.phone }}</a>
    </div>
    <div v-else id="theater-info">
      <div id="notice">
        지도에서 가까운 극장을 선택해주세요.
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'TicketTheater',
  props: {
    selectedTheater: Object,
  },
  data() {
    return {
      isSelected: false,
    }
  },
  watch: {
    selectedTheater: function() {
      this.isSelected = true
    }
  },
}
</script>

<style lang="scss">
  @import './TicketTheater.scss';
</style>