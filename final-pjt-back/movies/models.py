from django.db import models

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
    video_path = models.CharField(max_length=100)   # 유튜브 비디오 ID
    
    # 보고싶어요 mtm
    # 평점 mtm
    
    # 장르 mtm
    # 배우 mtm
    # 감독 mtm
    
    
class Review(models.Model): # 리뷰
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    movie_id = models.IntegerField()
    user_id = models.IntegerField()

class comment(models.Model): # 리뷰
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Rating(models.Model): # 별점
    movie_id = models.IntegerField()
    user_id = models.IntegerField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Genre(models.Model): # 장르 DB
    genre_id = models.IntegerField()
    genre_name = models.CharField(max_length=50)
    
class Actor(models.Model): # 장르 DB
    actor_id = models.IntegerField()
    actor_name = models.CharField(max_length=50)
    actor_popularity = models.FloatField()  # 배우 인기도
    actor_profile_path = models.TextField() # 프로필사진 이미지 주소
    
class Director(models.Model): # 장르 DB
    director_id = models.IntegerField()
    director_name = models.CharField(max_length=50)
    director_popularity = models.FloatField()  # 감독 인기도
    director_profile_path = models.TextField() # 프로필사진 이미지 주소
