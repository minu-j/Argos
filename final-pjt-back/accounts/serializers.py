from rest_framework import serializers
from movies.models import *
from .models import *

from django.contrib.auth import get_user_model

User = get_user_model()

# # 평점을 남긴 영화 목록
# class UserRatedSerializers(serializers.ModelSerializer):  

#     class MovieListSerializer(serializers.ModelSerializer):
        
#         # 영화에 별점을 준 사용자도 같이 가져오기
#         class RatedUserSerializer(serializers.ModelSerializer): 
            
#             # 별점 정보
#             class RatingListSerializer(serializers.ModelSerializer):

#                 class Meta:
#                     model = Rating
#                     fields = ('score',)
        
#             user_rating = RatingListSerializer(many=True)
        
#             class Meta:
#                 model = User
#                 fields = ('username', 'user_rating')
                
#         rated_users = RatedUserSerializer(many=True, read_only=True)

#         class Meta:
#             model = Movie
#             fields = '__all__'
    
#     rated_movies = MovieListSerializer(many=True, read_only=True)
    
#     class Meta:
#         model = User
#         fields = '__all__'


# 사용자가 평점을 준 영화 목록 조회
class UserMovieListSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = '__all__'

    user_rating = MovieSerializer(many=True)

    class Meta:
        model = User
        # 사용자 id, 평가한 영화 목록, 좋아요한 영화 목록, 위시리스트에 담은 영화 목록
        fields = '__all__'