from django.db import models
from django.conf import settings

# 영화 정보 DB - 영화와 N:M 관계
class Actor(models.Model): # 배우 DB
    id = models.IntegerField()
    name = models.CharField(max_length=50)
    popularity = models.FloatField()  # 배우 인기도
    profile_path = models.TextField() # 프로필사진 이미지 주소
    

class Director(models.Model): # 감독 DB
    id = models.IntegerField()
    name = models.CharField(max_length=50)
    popularity = models.FloatField()  # 감독 인기도
    profile_path = models.TextField() # 프로필사진 이미지 주소


class Genre(models.Model): # 장르 DB
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Provider(models.Model): # 공급 DB
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Keyword(models.Model): # 키워드 DB
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Movie(models.Model): # 영화 DB
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.CharField(max_length=100)
    popularity = models.FloatField()
    vote_average = models.FloatField()

    poster_path = models.TextField()                # 포스터 이미지 주소
    backdrop_path = models.TextField()              # 배경 이미지 주소
    video_path = models.CharField(max_length=100)   # 예고편 유튜브 ID
    
    # 유저와 영화 관계 N:M 필드
    wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="wish_movies", blank=True) # 보고싶어요 한 유저
    rated_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="rated_movies", through="Rating") # 유저의 평가 - 별점 스키마 별도 작성
    
    # 비슷한 영화 추천용 N:M필드
    actors = models.ManyToManyField(Actor)
    directors = models.ManyToManyField(Director)
    genres = models.ManyToManyField(Genre)
    providers = models.ManyToManyField(Provider)
    keyworks = models.ManyToManyField(Keyword)


class Rating(models.Model): # 별점
    movie_id = models.IntegerField()
    user_id = models.IntegerField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    
class Review(models.Model): # 리뷰
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    movie_id = models.IntegerField()
    user_id = models.IntegerField()


class comment(models.Model): # 리뷰의 댓글
    review = models.ForeignKey(Review, on_delete=models.CASCADE) # 리뷰 외부키
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
