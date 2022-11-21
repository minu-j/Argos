from rest_framework import serializers
from .models import *

from django.contrib.auth import get_user_model

User = get_user_model()

# 유저 정보
class UserSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = User
        fields = ('id', 'username',)


############################ 영화 정보 ############################


class GenreListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'


class ActorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'


class DirectorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Director
        fields = '__all__'


class KeywordListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Keyword
        fields = '__all__'


class VideoListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video
        fields = '__all__'


class ProviderListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Provider
        fields = '__all__'


############################ 영화 조회 ############################


# 전체 영화의 모든 속성 리스트 조회
class AllMovieListSerializer(serializers.ModelSerializer): 
    genres = GenreListSerializer(many=True, read_only=True)
    actors = ActorListSerializer(many=True, read_only=True)
    directors = DirectorListSerializer(many=True, read_only=True)
    keywords = KeywordListSerializer(many=True, read_only=True)
    videos = VideoListSerializer(many=True, read_only=True)
    providers = ProviderListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'


# 전체 영화 리스트 조회
class MovieListSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Movie
        fields = '__all__'
        

# 전체 영화 id, 제목, 포스터 주소만 조회
class MovieSearchSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('pk', 'id', 'title', 'poster_path', 'backdrop_path')
        

# 단일 영화 항목 조회
class MovieSerializer(serializers.ModelSerializer):
    genres = GenreListSerializer(many=True, read_only=True)
    actors = ActorListSerializer(many=True, read_only=True)
    directors = DirectorListSerializer(many=True, read_only=True)
    keywords = KeywordListSerializer(many=True, read_only=True)
    videos = VideoListSerializer(many=True, read_only=True)
    providers = ProviderListSerializer(many=True, read_only=True)
    
    # 영화 가져올때 해당 영화의 리뷰도 함께 가져오기
    class ReviewListSerializer(serializers.ModelSerializer):

        class CommentListSerializer(serializers.ModelSerializer):

            user = UserSerializer()
        
            class Meta:
                model = Comment
                fields = '__all__'
        
        comment_set = CommentListSerializer(many=True, read_only=True)

        user = UserSerializer()
        
        class Meta:
            model = Review
            fields = '__all__'
            
    review_set = ReviewListSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)
    
    
    # 영화에 별점을 준 사용자도 같이 가져오기
    class RatedUserSerializer(serializers.ModelSerializer): 
        
        # 별점 정보
        class RatingListSerializer(serializers.ModelSerializer):

            class Meta:
                model = Rating
                fields = fields = ('score',)
    
        user_rating = RatingListSerializer(many=True)
    
        class Meta:
            model = User
            fields = ('id', 'username', 'user_rating')
            
    rated_users = RatedUserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


########################### 장르 ######################################

class GenreMovieSerializer(serializers.ModelSerializer):
    movie_set = MovieSearchSerializer(many=True, read_only=True)
    
    class Meta:
        model = Genre
        fields = '__all__'



########################### 배우 ######################################

class ActorMovieSerializer(serializers.ModelSerializer):
    movie_set = MovieSearchSerializer(many=True, read_only=True)
    
    class Meta:
        model = Actor
        fields = '__all__'



########################### 감독 ######################################

class DirectorMovieSerializer(serializers.ModelSerializer):
    movie_set = MovieSearchSerializer(many=True, read_only=True)
    
    class Meta:
        model = Director
        fields = '__all__'



########################### 키워드 ######################################

class KeywordMovieSerializer(serializers.ModelSerializer):
    movie_set = MovieSearchSerializer(many=True, read_only=True)
    
    class Meta:
        model = Keyword
        fields = '__all__'



########################### 예고편 ######################################

class VideoMovieSerializer(serializers.ModelSerializer):
    movie_set = MovieSearchSerializer(many=True, read_only=True)
    
    class Meta:
        model = Video
        fields = '__all__'



########################### 공급자 ######################################

class ProviderMovieSerializer(serializers.ModelSerializer):
    movie_set = MovieSearchSerializer(many=True, read_only=True)
    
    class Meta:
        model = Provider
        fields = '__all__'



############################ 별점 ############################
        

# 별점 조회, 작성, 삭제
class RatingSerializer(serializers.ModelSerializer):
    movie = MovieSearchSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Rating
        fields = '__all__'


############################ 리뷰 ############################


# 리뷰 조회, 작성, 수정, 삭제
class ReviewSerializer(serializers.ModelSerializer):
    
    class CommentListSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Comment
            fields = '__all__'
    
    comment_set = CommentListSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    movie = MovieSearchSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'


############################ 댓글 ############################


# 댓글 조회, 작성, 수정, 삭제
class CommentSerializer(serializers.ModelSerializer): 
    review = ReviewSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'