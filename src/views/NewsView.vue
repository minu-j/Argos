<template>
  <div class="newsTable">
    <div class="container newsTable-content">
      <div class="row newsTable-row">
        <div
          v-for="(news, index) in newsTable"
          :key="`news-${index}`"
          class="col-12 col-md-6 newsTable-content-col"
        >
          <a :href="news.link" target="_blank">
            <div
              class="newsTable-content-box"
              :style="`background-image: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.7)), url('${news.imgSrc}');`"
            >
              <div class="newsTable-content-text">
                <div class="newsTable-content-text-title">{{ news.title }}</div>
                <div class="newsTable-content-text-content">
                  {{ news.content }}
                </div>
                <div class="newsTable-content-text-time">{{ news.time }}</div>
              </div>
            </div>
          </a>
        </div>
      </div>
      <div id="loader-place" class="row"></div>
      <div id="get-next-row" class="row"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NewsView",
  props: {
    selectedTheater: Object,
  },
  data() {
    return {
      isSelected: false,
      newsTable: [],
      nowNewsPage: 0,
    };
  },
  methods: {
    getMoreNews() {
      this.createLoader();
      this.nowNewsPage++;
      this.$store.dispatch("getNews", this.nowNewsPage);
      setTimeout(() => {
        this.newsTable = this.$store.state.newsTable.slice(
          0,
          this.nowNewsPage * 24
        );
        console.log("this", this.newsTable);
        const loaderPlace = document.querySelector("#loader-place");
        loaderPlace.innerHTML = "";
      }, 2000);
    },
    createLoader() {
      const loaderPlace = document.querySelector("#loader-place");
      setTimeout(() => {
        // 로더 생성
        loaderPlace.innerHTML =
          `<div class="col-12 col-md-6" style="display: flex; justify-content: center;">
        <div style="border-radius: 20px; max-width: 400px; min-height: 250px; background-color: rgb(52, 52, 52); padding: 25px 30px 25px 30px; box-shadow: rgba(0, 0, 0, 0.147) 0px 5px 15px; margin-bottom: 40px;"><div>
            <div style="background-color: rgb(81, 81, 81); height: 43px; color: rgba(250, 235, 215, 0); border-radius: 20px; margin-bottom: 20px;">ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ</div>
            <div style="background-color: rgb(81, 81, 81); height: 25px; color: rgba(250, 235, 215, 0); border-radius: 20px;">ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ</div> </div>
        </div></div>`.repeat(6);
      }, 500);
    },
  },
  mounted() {
    // 뉴스를 계속 불러오기만 하면, 마운트할때마다 vuex 스토리지에 뉴스가 남아있고,
    // 새로운 계속 뉴스가 뒤로 쌓이는 오류가 있어서,
    // 뉴스 처음 들어올 때 그동안 쌓인 뉴스 날려주기.
    this.$store.dispatch("clearNews");
    this.createLoader();
    const targetNews = document.querySelector("#get-next-row");
    console.log(targetNews);

    const readLastNews = (entries) => {
      // Destructuring
      const [{ isIntersecting }] = entries;

      if (isIntersecting) {
        console.log(isIntersecting);
        // this.getMoreNews()
      }
    };

    // intersection observer 생성자 초기화 (관찰자)
    const io = new IntersectionObserver(readLastNews, {
      root: null,
      threshold: 0.5,
    });

    // NodeList의 각 요소들 감시 시작
    io.observe(targetNews);
  },
};
</script>
<style lang="scss" scoped>
@import "./NewsView.scss";
</style>
