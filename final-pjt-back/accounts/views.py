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
def user_rated_list(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    serializer = UserRatedSerializers(user)
    return Response(serializer.data)

# 사용자가 좋아요/위시리스트/평점을 준 영화 목록 조회
@api_view(['GET'])
def user_movie_list(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    print(user)