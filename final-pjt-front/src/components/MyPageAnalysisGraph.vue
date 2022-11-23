<template>
  <div>
    <div id="graph">
      <div id="graph-container">
        <div id="graph-title">회원님의 별점 분포</div>
        <div id="graph-container-space">
          <svg :width="width" :height="height">
            <path fill="none" stroke="#ffed75" stroke-width="3" :d="path"></path>
          </svg>
        </div>
        <div id="graph-score">
          <div id="graph-score-numbers">
            <span>1</span>
            <span>2</span>
            <span>3</span>
            <span>4</span>
            <span>5</span>
          </div>
        </div>
        <div id="graph-average">
          평균 ★{{this.average}}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as d3 from "d3"

export default {
  name: 'MyPageAnalysisGraph',
  data() {
    return {
      data: [],
      width: null,
      height: null,
      paddingBlock: 20,
      paddingInline: 0,
      average: null
    };
  },
  props: {
    userRating: Object,
  },
  computed: {
    path() {
      return this.line(this.data);
    },
    line() {
      return d3
        .line()
        .x((d, i) => this.xScale(i))
        .y((d) => this.ySclae(d))
        .curve(d3.curveMonotoneX)
    },
    xScale() {
      return d3
        .scaleLinear()
        .range([this.paddingInline, this.width - this.paddingInline])
        .domain(d3.extent(this.data, (d, i) => i));
    },
    ySclae() {
      return d3.scaleLinear().range([this.height - this.paddingBlock, this.paddingBlock]).domain([0, Math.max(...this.data)]);
    },
  },
  mounted() {
    const box = document.querySelector('#graph-container-space')

    this.width = box.clientWidth - 70
    this.height = box.clientHeight

    // this.data.push(this.userRating["1"].length)
    // this.data.push(this.userRating["2"].length)
    // this.data.push(this.userRating["3"].length)
    // this.data.push(this.userRating["4"].length)
    // this.data.push(this.userRating["5"].length)

    let allMovieCount = 0
    let allMovieAcc = 0
    for (let i = 1; i < 6; i++) {
      const movieCount = this.userRating[String(i)].length
      this.data.push(movieCount)
      allMovieCount += movieCount
      allMovieAcc += i * movieCount
    }

    this.average = ( allMovieAcc / allMovieCount ).toFixed(1)
  }
}
</script>

<style lang="scss" scoped>
  @import './MyPageAnalysisGraph.scss';
</style>