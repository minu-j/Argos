<template>
  <div>
    <get-location/>
    <ticket-map @search-result-theater="getSelectedTheater"/>
    <ticket-theater :selected-theater="selectedTheater"/>
    <ticket-table :selected-theater="selectedTheater"/>
  </div>
</template>

<script>
import GetLocation from "@/components/GetLocation.vue"
import TicketMap from '@/components/TicketMap.vue'
import TicketTheater from '@/components/TicketTheater.vue'
import TicketTable from '@/components/TicketTable.vue'

export default {
  components: { 
    GetLocation,
    TicketMap,
    TicketTheater,
    TicketTable,
  },
  name: 'TicketView',
  data() {
    return {
      selectedTheater: null
    }
  },
  methods: {
    getSelectedTheater(response) {
      this.selectedTheater = response
    }
  }
}
</script>

<style lang="scss">
@import "@/views/TicketView.scss";
</style>