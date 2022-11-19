from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404, get_list_or_404

# from rest_framework_jwt.authentication import JSONWebTokenAuthentication


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


#########################################################################
# 회원 탈퇴
@api_view(['POST'])
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return Response(request)


# 팔로우
@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication]) 사용법 모르겠움
@permission_classes([IsAuthenticated])
def follow(request, username):

    person = get_object_or_404(get_user_model(), username=username)
    user = request.user
    # 자기 자신은 팔로우 할 수 없기 때문에
    if person != user:
        # 내가 (request.user) 그 사람의 팔로워 목록에 있다면
        if person.followers.filter(pk=user.pk).exists():
            # 언팔로우
            person.followers.remove(user)
            follow = True
        else:
            # 팔로우
            person.followers.add(user)
            follow = False
        follow_status ={
            'follow':follow,
            'count':person.followers.count(),
        }
        return JsonResponse(follow_status)
    # return redirect('accounts:profile', person.username)
# import code for encoding urls and generating md5 hashes
# import urllib, hashlib # gravatar library


## 사용자 프로파일
@api_view(['get'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request, username):    
    person = get_object_or_404(get_user_model(), username=username)

    context ={
        'username': person.username,
        'created_at': person.date_joined,
        'followers':person.followers.count(),
        'followings':person.followings.count(),
        # 'email_hash':email_hash,
    }
    return JsonResponse(context)