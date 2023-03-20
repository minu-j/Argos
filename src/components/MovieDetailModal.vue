<template>
  <div>
    <div id="modal">
      <img id="detail-modal-close" @click="closeModal" src="@/assets/CloseIcon.png">
      <div id="detail-modal">
        <div class="container text-center" id="detail-modal-container">
          <!-- 감독용 제목 -->
          <div v-if="modalData.category === 'genre'" id="detail-modal-title">{{modalData.data.name}} 장르의 영화 {{ modalData.movie_set.movie_set.length }}편</div>
          <div v-if="modalData.category === 'director'" id="detail-modal-title">{{modalData.data.name}} 감독의 영화 {{ modalData.movie_set.movie_set.length }}편</div>
          <div v-if="modalData.category === 'actor'" id="detail-modal-title">{{modalData.data.name}} 배우의 영화 {{ modalData.movie_set.movie_set.length }}편</div>
          <div class="row" id="detail-modal-row">
            <div v-for="(movie, index) in modalData.movie_set.movie_set" :key="`modal-${index}`" class="col-6 col-sm-4 col-lg-3">
              <div @click="goDetail(movie.pk)" id="detail-modal-card">
                <div id="detail-modal-card-box">
                  <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" id="detail-modal-card-img" alt="">
                </div>
                <div id="detail-modal-card-title">{{ movie.title }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'MovieDetailModal',
  methods: {
    closeModal() {
      this.$emit('close-modal')
    },
    goDetail(id) {
      this.$emit('close-modal')
      this.$router.push(`/movie/${id}`)
      this.$router.go(this.$router.currentRoute)
    }
  },
  props: {
    modalData: Object
  },
}
</script>

<style lang="scss" scoped>
  @import './MovieDetailModal.scss';
</style>

