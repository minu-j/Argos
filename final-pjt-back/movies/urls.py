from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('movie/', views.movie_list), # 영화 리스트
    path('movie/<int:movie_pk>/', views.movie_detail), # 단일 영화
    
    path('movie/<int:movie_pk>/rating/', views.rating_create), # 별점 생성
    path('rating/<int:rating_pk>/', views.rating_detail), # 별점 조회, 삭제
    
    path('movie/<int:movie_pk>/review/', views.review_create), # 리뷰 생성
    path('review/<int:review_pk>/', views.review_detail), # 리뷰 조회, 삭제
    
    path('review/<int:review_pk>/comment/', views.comment_create), # 코멘트 생성
    path('comment/<int:comment_pk>/', views.comment_detail), # 코멘트 조회, 삭제
]
