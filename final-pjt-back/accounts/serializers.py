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
            fields = ('id', 'title', 'poster_path', 'backdrop_path', 'genres', 'actors', 'directors', 'keywords')

    movie = MovieSerializers()

    class Meta:
        model = Rating
        fields = '__all__'