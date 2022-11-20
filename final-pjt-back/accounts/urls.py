from django.urls import path
from . import views

app_name = 'accounts'
# 회원가입(POST) : account/signup/
# 프로필 정보 조회 및 수정(GET/PUT) : account/user
# 비밀번호 번형(POST) : account/password/change/
# 비밀번호 찾기(POST) : account/password/reset/

urlpatterns = [
   path('userinfo/<str:username>/', views.get_user_info), # 로그인시 유저 정보 조회
   path('rating/<int:movie_pk>/<int:user_pk>/', views.get_user_rating), # 유저의 단일영화 별점 조회
   path('recommend/<int:user_pk>/', views.get_user_recommend), # 사용자의 추천 영화 반환
]
