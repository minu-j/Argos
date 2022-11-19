from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import *

User = get_user_model()

@api_view(['GET'])
 # 로그인시 유저 정보 조회
def get_user_info(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserInfoSerializers(user)
    return Response(serializer.data)

# 사용자가 평점 준 전체 목록 조회
@api_view(['GET'])
def get_user_rating_list(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserRatingListSerializers(user)
    return Response(serializer.data)

# 사용자가 단일 영화에 준 평점 조회
@api_view(['GET'])
def get_user_rating(request, movie_pk, user_pk):
    rating = get_object_or_404(Rating, movie_id=movie_pk, user_id=user_pk)
    serializer = RatingSerializers(rating)
    return Response(serializer.data)
