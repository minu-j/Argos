import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    kakaoMap: null,
    userLocation: { // 사용자 위치정보
      latitude: null,
      longitude: null,
    },
  },
  getters: {
  },
  mutations: {
    GET_LOCATION(state, payload) { // 위치정보 수집
      state.userLocation.latitude = payload.latitude
      state.userLocation.longitude = payload.longitude
    },
    CREATE_MAP(state, payload) { // 지도 생성
      state.kakaoMap = payload
    }
  },
  actions: {
    initMap(context) {
      /* global kakao */
      // 사용자 좌표 설정
      const latitude = context.state.userLocation.latitude
      const longitude = context.state.userLocation.longitude

      // 지도 위치 지정, 옵션 값 설정
      const kakaoMap = document.querySelector('#map')
      const mapOption = { 
        center: new kakao.maps.LatLng(latitude, longitude), // 지도의 중심좌표
        level: 6 // 지도의 확대 레벨
      }

      // 지도 생성 함수 호출
      context.commit('CREATE_MAP', new kakao.maps.Map(kakaoMap, mapOption))
    }
  },
  modules: {
  }
})
