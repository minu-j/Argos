from django.db import models

# 영화 DB
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.CharField(max_length=100)
    popularity = models.FloatField()
    vote_average = models.FloatField()
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    video_path = models.CharField(max_length=100)
    

# 리뷰
class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    movie_id = models.IntegerField()
    user_id = models.IntegerField()
    

# 별점
class Rating(models.Model):
    star = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    movie_id = models.IntegerField()
    user_id = models.IntegerField()
