from django.urls import path
from . import views

app_name = 'accounts'
# 회원가입(POST) : account/signup/
# 프로필 정보 조회 및 수정(GET/PUT) : account/user
# 비밀번호 번형(POST) : account/password/change/
# 비밀번호 찾기(POST) : account/password/reset/

urlpatterns = [
   path('userinfo/<str:username>/', views.get_user_info), # 로그인시 유저 정보 조회
   path('prifile/rating/<int:user_pk>/', views.get_user_rating_list), # 사용자가 별점 준 영화 모아보기
   path('rating/<int:movie_pk>/<int:user_pk>/', views.get_user_rating), # 유저의 단일영화 별점 조회

   path('delete/', views.delete, name='delete'),  # 회원 탈퇴
   path('profile/<str:username>/', views.profile, name='profile'),
   path('follow/<str:username>/', views.follow, name='follow'),   # 팔로우..
]  
