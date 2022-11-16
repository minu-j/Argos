from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers.account_ser import *
from rest_framework import status
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404

User = get_user_model()

# 회원가입
# 인증 필요 없이 접근 가능한 영역 : 추후 인증 필요
@api_view(['POST'])
def signup(request):
    serializer = AccountSignUpSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 회원탈퇴
@api_view(['POST'])

def user_delete(request):
    request.user.delete()
    data = {
            'content': f'{request.user}님의 탈퇴처리가 완료되었습니다.',
        }
    return Response(data, status=status.HTTP_204_NO_CONTENT)

# 사용자가 좋아요/위시리스트/평점을 준 영화 목록 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def user_movie_list(request, user_pk):
    Users = get_object_or_404(User, pk=user_pk)
    serializer = UserMovieListSerializer(Users)
    user_list = {
        'id' : serializer.data.get('id'),
        'user_rated_movie_count' : Users.user_rated_movie.count(),
        'user_rated_movie' : serializer.data.get('user_rated_movie'),
        'like_movies_count' : Users.like_movies.count(),
        'like_movies' : serializer.data.get('like_movies'),
        'wish_moives_count' : Users.wish_moives.count(),
        'wish_moives' : serializer.data.get('wish_moives'),
    }
    return JsonResponse(user_list)