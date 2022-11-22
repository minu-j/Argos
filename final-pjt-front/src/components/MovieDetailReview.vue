<template>
  <div>
    <div id="review-container" class="container">
      <div id="review-title">이 영화의 리뷰 {{movieData.review_count}}개</div>
      <div class="row">
        <div @click="openReview(null)" class="col-12 col-sm-6 col-lg-4 review">
          <div class="review-box">
            <div>
              <div v-if="userScore > 0">
                <span class="review-gold" v-for="(goldstar, index) in userScore" :key="`goldstar-${index}`">★</span>
                <span class="review-silver" v-for="(silverstar, index) in 5 - userScore" :key="`silverstar-${index}`">★</span>
              </div>
              <span v-else class="review-silver">별점이 입력되지 않았어요</span>
            </div>
            <textarea @keyup.enter="createReview" name="" id="review-textarea" rows="5" placeholder="이 영화의 한줄평"></textarea>
            <button id="review-button" @click="createReview">저장</button>
          </div>
        </div>
        <div @click="openReview(review.id)" v-for="(review, index) in [...movieData.review_set].reverse()" :key="`review-${index}`" class="col-12 col-sm-6 col-lg-4 review">
          <div class="review-box">
            <div>
              <span class="review-gold" v-for="(goldstar, index) in review.score" :key="`goldstar-${index}`">★</span>
              <span class="review-silver" v-for="(silverstar, index) in 5 - review.score" :key="`silverstar-${index}`">★</span>
            </div>
            <div v-show="editReviewId !== review.id">
              <!-- 해당 리뷰를 선택 안했을때는 리뷰 간략하게 표시하기 -->
              <div v-show="commentList.id !== review.id" :id="`review-${review.id}`" class="review-content-small">{{review.content}}</div>
              <div v-show="commentList.id === review.id" class="review-content">{{review.content}}</div>
            </div>
            <div v-show="editReviewId === review.id">
              <!-- 수정시 입력창 -->
              <textarea @keyup.enter="editReview(review.id)" name="" class="review-edit-textarea" :id="`review-edit-textarea-${review.id}`" rows="5"></textarea>
            </div>

            <!-- 내가 쓴 리뷰일 때 내 리뷰 표시하기 -->
            <div v-if="myUserName === review.user.username">
              <div class="review-my">
                <span class="review-username-my">내 리뷰</span>
                <!-- 댓글 수정버튼 -->
                <span  v-if="editReviewId !== review.id" @click="editReviewOpen(review.id)" class="review-username-my-edit">수정</span>
                <!-- 해당 댓글이 수정중일때는 취소버튼 표시 -->
                <span v-else @click="cancleEditReview" class="review-username-my-edit">취소</span>
                <!-- 댓글 삭제버튼 -->
                <span  v-if="editReviewId !== review.id" @click="deleteReview(review.id)" class="review-username-my-delete">삭제</span>
                <span v-else @click="editReview(review.id)" class="review-username-my-save">저장</span>
              </div>
            </div>
            <div v-else>
              <div @click="goProfile(review.user.username)" class="review-username">{{review.user.username}}</div>
            </div>
            <div class="review-create">
              <span>{{review.created_at.slice(0, 10)}}</span>
              <span> · 댓글 {{ review.comment_set.length }}</span>
            </div>
            <!-- 해당 리뷰를 선택했을 때만 코멘트 보이기 -->
            <div v-if="commentList.id === review.id">
              <div v-for="(comment, index) in review.comment_set" :key="`comment-${index}`">
                <div>
                  <!-- 내 코멘트랑 상대방 코멘트 다르게 표시하기 -->
                  <div v-if="comment.user.username !== myUserName">
                    <span class="comment-content">{{comment.content}}</span>
                    <div class="comment-create">
                      <span @click="goProfile(comment.user.username)">{{comment.user.username}}</span>
                      <span> · {{comment.created_at.slice(0, 10)}}</span>
                    </div>
                  </div>
                  <div v-else class="comment-my">
                    <span class="comment-content-my">{{comment.content}}</span>
                    <div class="comment-create-my">
                      <span>내 댓글</span>
                      <span> · {{comment.created_at.slice(0, 10)}}</span>
                      <span class="comment-create-my-delete" @click="deleteComment(comment.id)">삭제</span>
                    </div>
                  </div>
                </div>
              </div>
              <input class="comment-input" @keyup.enter="createComment(review.id)" placeholder="댓글을 입력하세요" :id="`input-${review.id}`" type="text">
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieDetailReview',
  props: {
    movieData: Object,
    userScore: Number
  },
  data() {
    return {
      commentList: {
        id: null,
        data: []
      },
      myUserName: null,
      editReviewId: null
    }
  },
  methods: {
    // 리뷰 생성
    createReview() {
      // 별점이 없으면 리뷰 작성 막기
      if (!this.userScore) {
        alert('먼저 이 영화를 평가해주세요')
      } else { // 별점 작성
        const API_URL = 'http://127.0.0.1:8000'
        const movie_id = this.movieData.id
        const Token = this.$store.state.token
        const reviewTextarea = document.querySelector('#review-textarea')
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/movie/${movie_id}/review/`,
          data: { 
            content: reviewTextarea.value,
            score: this.userScore
          },
          headers: {
            Authorization: `Token ${Token}`
          },
        })
          .then(res => {
            console.log('리뷰 작성', res.data)
            this.$emit('reload-movie-data')
            document.querySelector('#review-textarea').value = ''
          })
          .catch(err => {
            console.log(err)
          })
        
      }
    },
    // 리뷰 코멘트 열기
    openReview(id) {
      this.commentList.id = id
    },

    // 코멘트 생성
    createComment(id) {
      const API_URL = 'http://127.0.0.1:8000'
      const Token = this.$store.state.token
      const commentData = document.querySelector(`#input-${id}`).value
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/review/${id}/comment/`,
        data: { 
          content: commentData
        },
        headers: {
          Authorization: `Token ${Token}`
        },
      })
        .then(res => {
          console.log(res.data)
          this.$emit('reload-movie-data')
        })
        .catch(err => {
          console.log(err)
        })
      
      document.querySelector(`#input-${id}`).value = ''
    },

    // 코멘트 삭제
    deleteComment(id) {
      const API_URL = 'http://127.0.0.1:8000'
      const Token = this.$store.state.token
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/comment/${id}/`,
        headers: {
          Authorization: `Token ${Token}`
        },
      })
        .then(res => {
          console.log('코멘트 삭제', res.data)
          this.$emit('reload-movie-data')
        })
        .catch(err => {
          console.log(err)
        })
    },

    // 상대방 프로필로 이동
    goProfile(username) {
      this.$router.push(`/mypage/${username}`)
    },

    // 리뷰 수정창 열기
    editReviewOpen(id) {
      this.editReviewId = id
      const editTextarea = document.querySelector(`#review-edit-textarea-${id}`)
      const originalReview = document.querySelector(`#review-${id}`)
      console.log(editTextarea, originalReview)
      editTextarea.value = originalReview.innerText
    },

    // 리뷰 수정
    editReview(id) {
      console.log(id)
      const API_URL = 'http://127.0.0.1:8000'
      const Token = this.$store.state.token
      const reviewEditData = document.querySelector(`#review-edit-textarea-${id}`).value
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/review/${id}/`,
        data: { 
          content: reviewEditData,
          score: this.userScore
        },
        headers: {
          Authorization: `Token ${Token}`
        },
      })
        .then(res => {
          console.log(res.data)
          this.$emit('reload-movie-data')
          this.cancleEditReview()
        })
        .catch(err => {
          console.log(err)
        })
    },

    // 리뷰 수정 취소
    cancleEditReview() {
      this.editReviewId = null
    },

    // 리뷰 삭제
    deleteReview(id) {
      const API_URL = 'http://127.0.0.1:8000'
      const Token = this.$store.state.token
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/review/${id}/`,
        headers: {
          Authorization: `Token ${Token}`
        },
      })
        .then(res => {
          console.log('리뷰 삭제', res.data)
          this.$emit('reload-movie-data')
        })
        .catch(err => {
          console.log(err)
        })
      
    }
  },
  mounted() {
    this.myUserName = this.$store.state.username
  }
}
</script>

<style lang="scss" scoped>
  @import './MovieDetailReview.scss';
</style>