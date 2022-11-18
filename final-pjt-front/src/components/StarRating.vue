<template>
  <span class="star-box">
    <span v-if="!score.length">
      <svg id="star-1" @click="rating(1)" @mouseover="getGold(1)" @mouseleave="clearGold" xmlns="http://www.w3.org/2000/svg" width="44" height="44" fill="#eee" class="star"><g><path d="M22 33.444L9.83 42.327c-.784.572-1.842-.196-1.539-1.118l4.687-14.32L.769 18.06c-.787-.569-.383-1.812.588-1.81l15.067.033 4.624-14.34c.298-.924 1.606-.924 1.904 0l4.624 14.34 15.067-.033c.971-.002 1.375 1.241.588 1.81l-12.209 8.829 4.688 14.32c.302.922-.756 1.69-1.54 1.118L22 33.444z"></path></g></svg>
      <svg id="star-2" @click="rating(2)" @mouseover="getGold(2)" @mouseleave="clearGold" xmlns="http://www.w3.org/2000/svg" width="44" height="44" fill="#eee" class="star"><g><path d="M22 33.444L9.83 42.327c-.784.572-1.842-.196-1.539-1.118l4.687-14.32L.769 18.06c-.787-.569-.383-1.812.588-1.81l15.067.033 4.624-14.34c.298-.924 1.606-.924 1.904 0l4.624 14.34 15.067-.033c.971-.002 1.375 1.241.588 1.81l-12.209 8.829 4.688 14.32c.302.922-.756 1.69-1.54 1.118L22 33.444z"></path></g></svg>
      <svg id="star-3" @click="rating(3)" @mouseover="getGold(3)" @mouseleave="clearGold" xmlns="http://www.w3.org/2000/svg" width="44" height="44" fill="#eee" class="star"><g><path d="M22 33.444L9.83 42.327c-.784.572-1.842-.196-1.539-1.118l4.687-14.32L.769 18.06c-.787-.569-.383-1.812.588-1.81l15.067.033 4.624-14.34c.298-.924 1.606-.924 1.904 0l4.624 14.34 15.067-.033c.971-.002 1.375 1.241.588 1.81l-12.209 8.829 4.688 14.32c.302.922-.756 1.69-1.54 1.118L22 33.444z"></path></g></svg>
      <svg id="star-4" @click="rating(4)" @mouseover="getGold(4)" @mouseleave="clearGold" xmlns="http://www.w3.org/2000/svg" width="44" height="44" fill="#eee" class="star"><g><path d="M22 33.444L9.83 42.327c-.784.572-1.842-.196-1.539-1.118l4.687-14.32L.769 18.06c-.787-.569-.383-1.812.588-1.81l15.067.033 4.624-14.34c.298-.924 1.606-.924 1.904 0l4.624 14.34 15.067-.033c.971-.002 1.375 1.241.588 1.81l-12.209 8.829 4.688 14.32c.302.922-.756 1.69-1.54 1.118L22 33.444z"></path></g></svg>
      <svg id="star-5" @click="rating(5)" @mouseover="getGold(5)" @mouseleave="clearGold" xmlns="http://www.w3.org/2000/svg" width="44" height="44" fill="#eee" class="star"><g><path d="M22 33.444L9.83 42.327c-.784.572-1.842-.196-1.539-1.118l4.687-14.32L.769 18.06c-.787-.569-.383-1.812.588-1.81l15.067.033 4.624-14.34c.298-.924 1.606-.924 1.904 0l4.624 14.34 15.067-.033c.971-.002 1.375 1.241.588 1.81l-12.209 8.829 4.688 14.32c.302.922-.756 1.69-1.54 1.118L22 33.444z"></path></g></svg>
    </span>
    <span v-if="score.length" @click="clearRating" @mouseover="readyClearRating" @mouseleave="cancelReadyClearRating">
      <svg class="goldStar star" v-for="(index) in score" :key="`score-${index}`" xmlns="http://www.w3.org/2000/svg" width="44" height="44" fill="#ffed75"><g><path d="M22 33.444L9.83 42.327c-.784.572-1.842-.196-1.539-1.118l4.687-14.32L.769 18.06c-.787-.569-.383-1.812.588-1.81l15.067.033 4.624-14.34c.298-.924 1.606-.924 1.904 0l4.624 14.34 15.067-.033c.971-.002 1.375 1.241.588 1.81l-12.209 8.829 4.688 14.32c.302.922-.756 1.69-1.54 1.118L22 33.444z"></path></g></svg>
      <svg class="grayStar star" v-for="(index) in notScore" :key="`notScore-${index}`" xmlns="http://www.w3.org/2000/svg" width="44" height="44" fill="#eee"><g><path d="M22 33.444L9.83 42.327c-.784.572-1.842-.196-1.539-1.118l4.687-14.32L.769 18.06c-.787-.569-.383-1.812.588-1.81l15.067.033 4.624-14.34c.298-.924 1.606-.924 1.904 0l4.624 14.34 15.067-.033c.971-.002 1.375 1.241.588 1.81l-12.209 8.829 4.688 14.32c.302.922-.756 1.69-1.54 1.118L22 33.444z"></path></g></svg>
    </span>
  </span>
</template>

<script>
export default {
  name: 'StarRating',
  data() {
    return {
      score: [],
      notScore: [1, 2, 3, 4, 5],
    }
  },
  methods: {
    getGold(n) {
      for (let i = 1; i < n + 1; i++) {
        const star = document.querySelector(`#star-${i}`)
        star.setAttribute('fill', "#ffed75")
      }
    },
    clearGold() {
      for (let i = 1; i < 6; i++) {
        const star = document.querySelector(`#star-${i}`)
        star.setAttribute('fill', "#eee")
      }
    },
    rating(n) {
      for (let i = 1; i < n + 1; i++) {
        const star = document.querySelector(`#star-${i}`)
        star.removeAttribute('fill')
        star.setAttribute('fill', "#ffed75")
        this.score.push(i)
        this.notScore.pop()
      }
    },
    readyClearRating() {
      const goldStars = document.querySelectorAll('.goldStar')
      goldStars.forEach((goldStar) => {
        goldStar.removeAttribute('fill')
        goldStar.setAttribute('fill', "#f5eebf")
      })
    },
    cancelReadyClearRating() {
      const goldStars = document.querySelectorAll('.goldStar')
      goldStars.forEach((goldStar) => {
        goldStar.removeAttribute('fill')
        goldStar.setAttribute('fill', "#ffed75")
      })
    },
    clearRating() {
      this.score = []
      this.notScore = [1, 2, 3, 4, 5]
    }
  },
}
</script>

<style>
.star {
  margin-right: 5px;
}
.star:hover {
  cursor: pointer;
}
</style>