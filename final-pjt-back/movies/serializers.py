from rest_framework import serializers
from .models import *

from django.contrib.auth import get_user_model

User = get_user_model()

# 유저 정보
class UserSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = User
        fields = ('id', 'username',)


# 전체 영화 리스트 조회
class MovieListSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Movie
        fields = '__all__'
        

# 영화 pk, 제목만 조회
class MovieTitleSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('pk', 'title')
        

# 단일 영화 항목 조회
class MovieSerializer(serializers.ModelSerializer):
    
    # 영화 가져올때 해당 영화의 리뷰도 함께 가져오기
    class ReviewListSerializer(serializers.ModelSerializer):
        
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
            fields = ('username', 'user_rating')
            
    rated_users = RatedUserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        

# 별점 조회, 작성, 삭제
class RatingSerializer(serializers.ModelSerializer):

    movie = MovieTitleSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Rating
        fields = '__all__'


# 리뷰 조회, 작성, 수정, 삭제
class ReviewSerializer(serializers.ModelSerializer):
    
    class CommentListSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Comment
            fields = '__all__'
    
    comment_set = CommentListSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    movie = MovieTitleSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'


# 댓글 조회, 작성, 수정, 삭제
class CommentSerializer(serializers.ModelSerializer): 
    
    review = ReviewSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'