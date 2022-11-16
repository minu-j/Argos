from rest_framework import serializers
from .models import Movie, Review, Rating

class MovieListSerializer(serializers.ModelSerializer): # 영화 리스트
    
    class Meta:
        model = Movie
        fields = '__all__'