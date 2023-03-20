from django.db import models
from django.conf import settings

# 영화 정보 DB - 영화와 N:M 관계
class Actor(models.Model): # 배우 DB
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    popularity = models.FloatField()  # 배우 인기도
    profile_path = models.TextField(null=True, blank=True) # 프로필사진 이미지 주소
    

class Director(models.Model): # 감독 DB
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    popularity = models.FloatField()  # 감독 인기도
    profile_path = models.TextField(null=True, blank=True) # 프로필사진 이미지 주소


class Genre(models.Model): # 장르 DB
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Video(models.Model): # 장르 DB
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=200)
    key = models.CharField(max_length=50)
    video_type = models.CharField(max_length=50)


class Provider(models.Model): # 공급 DB
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    logo_path = models.CharField(max_length=100)
    display_priority = models.IntegerField()


class Keyword(models.Model): # 키워드 DB
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Movie(models.Model): # 영화 DB
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)        # 영화 제목
    original_title = models.CharField(max_length=100) # 원제
    overview = models.TextField()                   # 줄거리
    release_date = models.CharField(max_length=50)  # 개봉일
    popularity = models.FloatField()                # 인기도
    vote_average = models.FloatField()              # TMDB 평균 별점
    poster_path = models.TextField()                # 포스터 이미지 주소
    backdrop_path = models.TextField()              # 배경 이미지 주소

    runtime = models.TextField(null=True, blank=True)                    # 상영시간
    status = models.CharField(max_length=50, null=True, blank=True)        # 상태
    tagline = models.TextField(null=True, blank=True)                    # 슬로건

    # 유저와 영화 관계 N:M 필드
    rated_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="rated_movies", through="Rating", blank=True) # 유저의 평가 - 별점 스키마 별도 작성
    
    # 비슷한 영화 추천용 N:M필드
    genres = models.ManyToManyField(Genre, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)
    directors = models.ManyToManyField(Director, blank=True)
    keywords = models.ManyToManyField(Keyword, blank=True)
    videos = models.ManyToManyField(Video, blank=True)   # 예고편 유튜브 ID
    providers = models.ManyToManyField(Provider, blank=True)


class Rating(models.Model): # 별점용 중계 테이블
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_rating')
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    
class Review(models.Model): # 리뷰
    content = models.TextField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_review')


class Comment(models.Model): # 리뷰의 댓글 
    review = models.ForeignKey(Review, on_delete=models.CASCADE) # 리뷰 외부키
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comment')


class Playlist(models.Model): # 플레이리스트
    title = models.CharField(max_length=50)


class PlayMovie(models.Model): # 영화
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=50)
    key = models.CharField(max_length=50)
