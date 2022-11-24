from rest_framework import serializers
from movies.models import *
from .models import *

from django.contrib.auth import get_user_model

User = get_user_model()

# 로그인시 사용자 정보 획득용
class UserInfoSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = User
        fields = ('id', 'username',)


# 영화에 사용자가 준 별점
class RatingSerializers(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('id', 'user_id', 'score',)


class RatingListSerializers(serializers.ModelSerializer):

    class MovieSerializers(serializers.ModelSerializer):

        class GenreSerializers(serializers.ModelSerializer):

            class Meta:
                model = Genre
                fields = '__all__'
            
        genres = GenreSerializers(many=True)

        class ActorSerializers(serializers.ModelSerializer):

            class Meta:
                model = Actor
                fields = '__all__'
            
        actors = ActorSerializers(many=True)

        class DirectorSerializers(serializers.ModelSerializer):

            class Meta:
                model = Director
                fields = '__all__'
            
        directors = DirectorSerializers(many=True)

        class KeywordSerializers(serializers.ModelSerializer):

            class Meta:
                model = Keyword
                fields = '__all__'
            
        keywords = KeywordSerializers(many=True)

        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path', 'backdrop_path', 'genres', 'actors', 'directors', 'keywords', 'videos')

    movie = MovieSerializers()

    class Meta:
        model = Rating
        fields = '__all__'
        
        
############################ 유저가 작성한 리뷰, 코멘트 조회 #############################

class UserReviewSerializers(serializers.ModelSerializer):
    
    class CommentListSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Comment
            fields = '__all__'
    
    comment_set = CommentListSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class MovieSerializers(serializers.ModelSerializer):
    
        class Meta:
            model = Movie
            fields = ('id', 'title')
            
    movie = MovieSerializers()
    
    class Meta:
            model = Review
            fields = '__all__'
        
class UserCommentSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        
        
########################### 팔로우 #############################33
        

class UserFollowListSerializers(serializers.ModelSerializer):
    
    class UserListSerializers(serializers.ModelSerializer):

        class Meta:
            model = User
            fields = ('id', 'username')
            
    followings = UserListSerializers(many=True)
    following_count = serializers.IntegerField(source='followings.count', read_only=True)
    followers = UserListSerializers(many=True)
    follower_count = serializers.IntegerField(source='followers.count', read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'followers', 'follower_count', 'followings', 'following_count')