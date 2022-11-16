<template>
  <div>
    <get-location/>
    <ticket-map/>
  </div>
</template>

<script>
import GetLocation from "@/components/GetLocation.vue"
import TicketMap from '@/components/TicketMap.vue'

export default {
  components: { 
    GetLocation,
    TicketMap
  },
  name: 'TicketView',
}
</script>

<style lang="scss">
@import "@/views/TicketView.scss";

</style>