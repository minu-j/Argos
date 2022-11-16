<template>
  <div>
    <div id="map-container">
      <div id="map"></div>
    </div>
  </div>
</template>

<script>
</script>
<script>
export default {
  name: 'TicketMap',
    mounted() {
    if (!window.kakao || !window.kakao.maps) {
      const kakaoMapScript = document.createElement('script')
      kakaoMapScript.src = `//dapi.kakao.com/v2/maps/sdk.js?libraries=services,clusterer&autoload=false&appkey=${process.env.VUE_APP_KAKAO_API_KEY}`
      document.head.appendChild(kakaoMapScript)

      /* global kakao */
      kakaoMapScript.addEventListener("load", () => {
        kakao.maps.load(() => {
          console.log("지도 API가 로딩됨")
          this.$store.dispatch('initMap')

          // const searchPlaces = new kakao.maps.services.Places()

          // // 마커 추가용 clusterer 객체 선언
          // const clusterer = new kakao.maps.MarkerClusterer({
          //   map: this.map,
          // });

          // // 현재위치에 마커에 추가 
          // const markerImageUrl = 'https://drive.google.com/uc?export=view&id=1UNnAGTdpaGOytwtuPkiRZbmvPE_jTf8f', 
          // markerImageSize = new kakao.maps.Size(64, 64), // 마커 이미지의 크기
          // markerImageOptions = { 
          //   offset : new kakao.maps.Point(20, 20)// 마커 좌표에 일치시킬 이미지 안의 좌표
          // };
          // const markerImage = new kakao.maps.MarkerImage(markerImageUrl, markerImageSize, markerImageOptions);

          // const marker = new kakao.maps.Marker({
          //   position: new kakao.maps.LatLng(latitude, longitude),
          //   image: markerImage
          // })
          // clusterer.addMarker(marker)

          // // 현재 위치 기준으로 '영화관' 키워드 검색
          // searchPlaces.keywordSearch('영화관', (result, status) => {
          //   if (status === kakao.maps.services.Status.OK) {

          //     // CGV, 메가박스, 롯데시네마 결과만 가져오기
          //     result.map((searchResultTheater) => {

          //       // CGV
          //       if (searchResultTheater.category_name === "문화,예술 > 영화,영상 > 영화관 > CGV") {
          //         this.searchResult.push(searchResultTheater)

          //         // 해당 좌표에 CGV 마커 추가
          //         const markerImageUrl = 'https://drive.google.com/uc?export=view&id=1wh_dvmLsGBQoVmv43aK3rcMi11E56k7l', 
          //             markerImageSize = new kakao.maps.Size(64, 64), // 마커 이미지의 크기
          //             markerImageOptions = { 
          //                 offset : new kakao.maps.Point(20, 20)// 마커 좌표에 일치시킬 이미지 안의 좌표
          //             };
          //         const markerImage = new kakao.maps.MarkerImage(markerImageUrl, markerImageSize, markerImageOptions);

          //         const marker = new kakao.maps.Marker({
          //           position: new kakao.maps.LatLng(searchResultTheater.y, searchResultTheater.x),
          //           image: markerImage
          //         })

          //         // 마커에 커서가 오버됐을 때 마커 위에 표시할 인포윈도우를 생성합니다
          //         const iwContent = `<div style="padding:5px; overflow: hidden; white-space: nowrap; text-overflow: ellipsis;">${searchResultTheater.place_name}</div>` // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
          //         // 인포윈도우를 생성합니다
          //         const infowindow = new kakao.maps.InfoWindow({
          //             content : iwContent
          //         });
          //         // 마커에 마우스오버 이벤트를 등록합니다
          //         kakao.maps.event.addListener(marker, 'mouseover', () => {
          //           // 마커에 마우스오버 이벤트가 발생하면 인포윈도우를 마커위에 표시합니다
          //           infowindow.open(this.map, marker);
          //         })
          //         // 마커에 마우스아웃 이벤트를 등록합니다
          //         kakao.maps.event.addListener(marker, 'mouseout', () => {
          //           // 마커에 마우스아웃 이벤트가 발생하면 인포윈도우를 제거합니다
          //           infowindow.close();
          //         })
          //         // 클릭시 이벤트 등록
          //         kakao.maps.event.addListener(marker, 'click', () => {
          //           this.selectedTheater = searchResultTheater
          //           this.$emit('search-result-theater', searchResultTheater)
          //         })

          //         clusterer.addMarker(marker)

          //       // 메가박스
          //       } else if (searchResultTheater.category_name === "문화,예술 > 영화,영상 > 영화관 > 메가박스") {
          //         this.searchResult.push(searchResultTheater)
                
          //         // 해당 좌표에 메가박스 마커 추가
          //         const markerImageUrl = 'https://drive.google.com/uc?export=view&id=1STZmM3usto78Se5GWcm7hUwwv_636Fg5', 
          //             markerImageSize = new kakao.maps.Size(64, 64), // 마커 이미지의 크기
          //             markerImageOptions = { 
          //                 offset : new kakao.maps.Point(20, 20)// 마커 좌표에 일치시킬 이미지 안의 좌표
          //             };
          //         const markerImage = new kakao.maps.MarkerImage(markerImageUrl, markerImageSize, markerImageOptions);
                  
          //         const marker = new kakao.maps.Marker({
          //           position: new kakao.maps.LatLng(searchResultTheater.y, searchResultTheater.x),
          //           image: markerImage
          //         })
          //         // 마커에 커서가 오버됐을 때 마커 위에 표시할 인포윈도우를 생성합니다
          //         const iwContent = `<div style="padding:5px; overflow: hidden; white-space: nowrap; text-overflow: ellipsis;">${searchResultTheater.place_name}</div>` // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
          //         // 인포윈도우를 생성합니다
          //         const infowindow = new kakao.maps.InfoWindow({
          //             content : iwContent
          //         });
          //         // 마커에 마우스오버 이벤트를 등록합니다
          //         kakao.maps.event.addListener(marker, 'mouseover', () => {
          //           // 마커에 마우스오버 이벤트가 발생하면 인포윈도우를 마커위에 표시합니다
          //           infowindow.open(this.map, marker);
          //         })
          //         // 마커에 마우스아웃 이벤트를 등록합니다
          //         kakao.maps.event.addListener(marker, 'mouseout', () => {
          //           // 마커에 마우스아웃 이벤트가 발생하면 인포윈도우를 제거합니다
          //           infowindow.close();
          //         })
          //         // 클릭시 이벤트 등록
          //         kakao.maps.event.addListener(marker, 'click', () => {
          //           this.selectedTheater = searchResultTheater
          //           this.$emit('search-result-theater', searchResultTheater)
          //         })
          //         // 클릭시 이벤트 등록
          //         kakao.maps.event.addListener(marker, 'click', () => {
          //           this.selectedTheater = searchResultTheater
          //           this.$emit('search-result-theater', searchResultTheater)
          //         })
          //         clusterer.addMarker(marker)

          //       // 롯데시네마
          //       } else if (searchResultTheater.category_name === "문화,예술 > 영화,영상 > 영화관 > 롯데시네마") {
          //         this.searchResult.push(searchResultTheater)

          //         // 해당 좌표에 롯데시네마 마커 추가
          //         const markerImageUrl = 'https://drive.google.com/uc?export=view&id=11arz6kvt1C_mHEdH0GMpGSXjS5lUVqpL', 
          //             markerImageSize = new kakao.maps.Size(64, 64), // 마커 이미지의 크기
          //             markerImageOptions = { 
          //                 offset : new kakao.maps.Point(20, 20)// 마커 좌표에 일치시킬 이미지 안의 좌표
          //             };
          //         const markerImage = new kakao.maps.MarkerImage(markerImageUrl, markerImageSize, markerImageOptions);

          //         const marker = new kakao.maps.Marker({
          //           position: new kakao.maps.LatLng(searchResultTheater.y, searchResultTheater.x),
          //           image: markerImage
          //         })
          //         // 마커에 커서가 오버됐을 때 마커 위에 표시할 인포윈도우를 생성합니다
          //         const iwContent = `<div style="padding:5px; overflow: hidden; white-space: nowrap; text-overflow: ellipsis;">${searchResultTheater.place_name}</div>` // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
          //         // 인포윈도우를 생성합니다
          //         const infowindow = new kakao.maps.InfoWindow({
          //             content : iwContent
          //         });
          //         // 마커에 마우스오버 이벤트를 등록합니다
          //         kakao.maps.event.addListener(marker, 'mouseover', () => {
          //           // 마커에 마우스오버 이벤트가 발생하면 인포윈도우를 마커위에 표시합니다
          //           infowindow.open(this.map, marker);
          //         })
          //         // 마커에 마우스아웃 이벤트를 등록합니다
          //         kakao.maps.event.addListener(marker, 'mouseout', () => {
          //           // 마커에 마우스아웃 이벤트가 발생하면 인포윈도우를 제거합니다
          //           infowindow.close();
          //         })
          //         // 클릭시 이벤트 등록
          //         kakao.maps.event.addListener(marker, 'click', () => {
          //           this.selectedTheater = searchResultTheater
          //           this.$emit('search-result-theater', searchResultTheater)
          //         })
          //         clusterer.addMarker(marker)
          //       }
          //     })
          //     console.log(this.searchResult)
          //   } else {
          //     console.log('지도 검색 요청 실패')
          //   }
          // }, {
          //   location: new kakao.maps.LatLng(latitude, longitude)
          // })
        })
      })
    } else {
      console.log("지도가 이미 로딩됨")
      this.$store.dispatch('initMap')
    }
  }
}
</script>

<style lang="scss" scoped>
  @import './TicketMap.scss';
</style>