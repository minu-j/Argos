from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('movie/', views.all_movie_list), # 영화 리스트
    path('movie/<int:movie_pk>/', views.movie_detail), # 단일 영화
    path('movie/random/', views.get_movie_random), # 랜덤 영화

    path('movie/genre/', views.genre_list), # 장르 리스트
    path('movie/genre/<int:genre_pk>/', views.genre_detail), # 장르별 조회

    path('movie/actor/', views.actor_list), # 배우 리스트
    path('movie/actor/<int:actor_pk>/', views.actor_detail), # 배우별 조회

    path('movie/director/', views.director_list), # 감독 리스트
    path('movie/director/<int:director_pk>/', views.director_detail), # 감독별 조회

    path('movie/keyword/', views.keyword_list), # 키워드 리스트
    path('movie/keyword/<int:keyword_pk>/', views.keyword_detail), # 키워드별 조회

    path('movie/video/', views.video_list), # 예고편 리스트

    path('movie/provider/', views.provider_list), # 공급자 리스트
    path('movie/provider/<int:provider_pk>/', views.provider_detail), # 공급자별 조회
    
    path('movie/<int:movie_pk>/rating/', views.rating_create), # 별점 생성
    path('rating/<int:rating_pk>/', views.rating_detail), # 별점 조회, 삭제
    
    path('movie/<int:movie_pk>/review/', views.review_create), # 리뷰 생성
    path('review/<int:review_pk>/', views.review_detail), # 리뷰 조회, 수정 삭제
    
    path('review/<int:review_pk>/comment/', views.comment_create), # 코멘트 생성
    path('comment/<int:comment_pk>/', views.comment_detail), # 코멘트 조회, 삭제
]
