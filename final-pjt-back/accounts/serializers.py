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


class UserRatingListSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

# 해당 영화에 사용자가 준 별점
class RatingSerializers(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('id', 'user_id', 'score',)