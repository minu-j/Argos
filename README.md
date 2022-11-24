![](README_assets/2022-11-20-23-26-07-image.png)

![logo](README_assets/logo.gif)

<center><h1>ARGOS</h1></center> 

<center><strong>"영화를 찾는 눈"<strong></center> 

<center>SSAFY 8th Final Team Project</center> 

<br>

<center>ARGOS는 그리스 로마 신화에 등장하는 100개의 눈이 달린 감시자입니다.
<br>우리의 아르고스는 사용자에게 알맞는 영화를 정확히 찾아내는 멋진 눈을 가진 친구입니다.</center>


---


## 📚 목차

1. [개요](##-🌟-개요)

2. [팀](##-🧑🏻‍🤝‍🧑🏻-팀)
   
3. [서비스 소개](##-📽️-서비스-소개)
   
4. [설치 및 실행](##-🚀-설치-및-실행)
   
5. [오픈소스 출처](##-📃-오픈소스-출처)

---

## 🌟 개요

### 프로젝트 기간

2022.11.16 ~ 2022.11.24 (8일)

### 버전

  ![node.js](https://img.shields.io/badge/node.js-v16.17.1-brightgreen) ![npm](https://img.shields.io/badge/npm-v9.1.1-green) ![pip](https://img.shields.io/badge/pip-v22.0.4-blue)

### 기술 스택 👨‍💻 

- #### frontend
  
  ![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D)![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)![SASS](https://img.shields.io/badge/SASS-hotpink.svg?style=for-the-badge&logo=SASS&logoColor=white)![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
  

- #### backend
  
  ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


- #### Editors

  ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)


- #### Version Control

  ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
  
- #### Publishing

  Comming soon...

## 🧑🏻‍🤝‍🧑🏻 팀

|       |  Github  |  역할  |
|:------------:|:------------:|:------------:|
| **정민우** (조장)  |  [minu-j](https://github.com/minu-j/)  |  총괄, Frontend  |
| **김성훈** |  [kimseonghun96](https://github.com/kimseonghun96/)  |  Backend  |

---

## 📽️ 서비스 소개
  
### 기획 의도

**ARGOS**는 사용자의 별점 평가 척도에 기반하여, 유저가 선호하는 영화의 장르, 배우, 감독, 키워드 별 추천 영화를 유저에게 맞춤 제공하는 서비스입니다.

맞춤 영화 추천 외에도 영화 리뷰 기반 커뮤니티, 영화티켓 예매, 무료 영화 감상, 영화 관련 뉴스 피드 서비스를 제공하여 통합된 사용자 경험을 제공합니다.

### ERD

![loading-ag-860](README_assets/17445e000bc7a36639dbb85e72242a648f8489c3.png)

### WireFrame

![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)

![loading-ag-860](README_assets/wireframe.png)


### 구현 기능

---

## 🚀 설치 및 실행

1. Git Clone

```shell
$ git clone https://github.com/minu-j/Argos.git
```

2. Run Back-server
```shell
 ~/.../Argos/

$ cd final-pjt-back

$ python -m venv venv
$ source venv/Scripts/activate

$ python manage.py makemigrations
$ python manage.py migrate

$ python manage.py loaddata db_1.json
$ python manage.py loaddata db_2.json
$ python manage.py loaddata db_3.json

$ python manage.py runserver
```

3. Run Front-Server
```shell
 ~/.../Argos/

$ cd final-pjt-front/

$ npm install

$ npm run serve
```

4. Done!

---

## 📃 오픈소스 출처

#### Library

  ![Vuex](https://img.shields.io/badge/Vuex-v22.0.4-white)
  ![Router](https://img.shields.io/badge/Router-v22.0.4-white)
  ![Axios](https://img.shields.io/badge/Axios-v22.0.4-white)
  ![Cheerio](https://img.shields.io/badge/Cheerio-v22.0.4-white)
  ![Vue-Wordcloud](https://img.shields.io/badge/VueWordcloud-v22.0.4-white)
  ![D3](https://img.shields.io/badge/D3-v22.0.4-white)

#### API

  [TMDB]() - 영화 정보 검색

  [KOBIS]() - KOFIC 영화관 입장권 통합 전산망

  [KakaoMap]() - 카카오맵

#### etc...

[flaticon](https://www.flaticon.com/) - 아이콘


---

|     | 기능                    | 기능설명                                                                                          |
| --- | --------------------- | --------------------------------------------------------------------------------------------- |
| 1   | 회원 가입                 | 토큰을 통한 유저 회원 가입, 회원 가입 시 자동 로그인, 첫 로그인 시바로 영화 추천을 위한 영화 평가 페이지로 이동                            |
| 2   | 로그인                   | 토큰을 통한 인증 로그인 기능 구현                                                                           |
| 3   | 비 로그인 시               | 추천 영화 페이지 가리기 구현                                                                              |
| 4   | 로그아웃                  | isLogin을 이용해 토큰을 null 값으로 만듬                                                                  |
| 5   | 영화 검색 기능              | 검색하고 싶은 영화를 검색하면 그영화의 소개와 더 많은 정보를 알 수있는 링크 연결                                                |
| 6   | 팔로우, 팔로잉              | 유저간의 팔로우 및 팔로잉 기능 구현                                                                          |
| 7   | 마이페이지 조회              | 유저 정보, 별점을 준 영화, 별점을 기반으로 한 선호하는 키워드, 배우, 감독, 장르 통계 자료 편성, 유저의 팔로워, 팔로잉 확인, 리뷰 작성 목록 조회 기능 구현 |
| 8   | tmdb 자료 추출 및 DB화      | (몇 개의 영화가 어떤 식으로 구성되어 있는지 적으면 좋을 듯 )                                                          |
| 10  | 영화 별점 주기              | 내가 본 영화를 별의 개수로 평가하는 기능 구현, 많은 영화를 평가 할 수 있게 인피니티 스크롤 구현                                      |
| 11  | 비슷한 장르의 추천 영화 조회      | 높은 별점을 준 영화를 바탕으로 장르, 키워드, 배우, 감독 등 여러 영화 추천 기능 구현                                            |
| 12  | 단일 영화 페이지 조회          | 세부 영화 정보 표현, 트레일러 영상, 출연 배우, 감독 및 비슷한 영화 모음 기능 구현, 유저들이 작성한 리뷰들 모음 구현                         |
| 13  | 영화 메인 페이지 조회          | 박스 오피스 순위, 추천 영화 스와이프 형식으로 구현                                                                 |
| 14  | 무료 영화 시청할 수 있는 공간 제작  | 유튜브 고전 영화, 독립 영화 등                                                                            |
| 15  | 404 페이지 기능            | 없는 URL로 요청시 404 page로 push 구현                                                                 |
| 16  | 리뷰 생성/ 삭제             | 특정 영화의 리뷰 생성 기능 및 삭제 구현                                                                       |
| 17  | 다른 유저의 리뷰에 대댓글 생성/ 삭제 | 특정 리뷰의 댓글 생성 기능 및 삭제 구현                                                                       |
| 18  | 영화관 시간표 조회 및 예매 링크 연결 | 위치기반 조회(지도 API, 예매시간표 ), 선택 상영관 조회(전국 영화관 DB)                                                 |
| 19  | 영화 관련 추천 뉴스           | 실시간으로 영화와 관련된 기사들을 볼 수 있는 공간 구현(웹 크롤링)                                                        |

## 소개(영상이나 사진 사용)

### 도입페이지

### 홈 화면 각종 반응형 모음집 1탄 ㅎ

![홈 화면 각종 반응형 모음집 1탄.gif](README_assets/72640e8e76f471980e3e6a8565755c06634a7a4e.gif)

### 박스오피스

![박스오피스_gif.gif](README_assets/cb4a6dd644f51f39528d7c365b6ed77e1ef65f45.gif)

### 회원가입

![회원 가입부터 영화 평가까지.gif](README_assets/64e0372ad006cf179cb7d12133ef4bdcd8b4bfcc.gif)

### 영화 상세페이지 리뷰 전까지

![영화 상세페이지 리뷰 전까지.gif](README_assets/28dfc65d8bc4833f85bb159755ab4ea3a1cb570a.gif)

### 리뷰 작성

![영화 상세페이지 리뷰_gif (2).gif](README_assets/041df7aec1037e97c6c3a84d0c54eafed9db904e.gif)

### 영화관 시간표 조회 및 예매 링크 연결

![지도와 티켓.gif](README_assets/23fdb4a9d64a02377d3954fb64d4e55ad6a47446.gif)

### 영화 관련 기사 모음

![영화 기사 관련.gif](README_assets/67cb623099dc569dfec3c9567bdb5ec8f3afb763.gif)

### 

### 검색기능

![검색기능.gif](README_assets/8426dc3e068f9591afadcc8f90eda05eb242acb3.gif)

### 404page

- ## 

## 느낀점

### 정민우

### 김성훈