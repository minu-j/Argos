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
   path('analysis/<str:username>/', views.get_user_analysis), # 사용자의 취향정보, 그동안 평가한 영화 반환
   path('review/<str:username>/', views.get_user_review), # 사용자의 취향정보, 그동안 평가한 영화 반환
   path('comment/<str:username>/', views.get_user_comment), # 사용자의 취향정보, 그동안 평가한 영화 반환

   path('delete/', views.delete, name='delete'),  # 회원 탈퇴
   path('follow/<str:username>/', views.follow, name='follow'),   # 팔로우..
   path('follow/list/<str:username>/', views.get_user_follow),   # 해당 회원의 팔로잉, 팔로워
]
