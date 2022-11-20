from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404, get_list_or_404
from collections import defaultdict

from .serializers import *

User = get_user_model()

 # 로그인시 유저 정보 조회
@api_view(['GET'])
def get_user_info(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserInfoSerializers(user)
    return Response(serializer.data)

# 사용자가 단일 영화에 준 평점 조회
@api_view(['GET'])
def get_user_rating(request, movie_pk, user_pk):
    rating = get_object_or_404(Rating, movie_id=movie_pk, user_id=user_pk)
    serializer = RatingSerializers(rating)
    return Response(serializer.data)

################################## 영화추천 알고리즘 ##################################

# 유저가 준 모든 평점의 영화 리스트를 기반으로 취향을 계산하여 반환
@api_view(['GET'])
def get_user_recommend(request, user_pk):
    ratings = get_list_or_404(Rating, user_id=user_pk)
    serializer = RatingListSerializers(ratings, many=True)

    # 반환할 객체
    response_data = {
        'rating': {
            1: [],
            2: [],
            3: [],
            4: [],
            5: []
        },
        ### 4점 이상 준 영화와 매칭되는 특징을 정리
        # 각 영화를 순회하면서 별점이 높은 특징을 딕셔너리로 만들기
        'like_genre': defaultdict(int), # 좋아하는 장르
        'like_actor': defaultdict(int), # 좋아하는 배우
        'like_director': defaultdict(int), # 좋아하는 감독
        'like_keyword': defaultdict(int) # 좋아하는 키워드    
    }

    for rating in serializer.data:
        movie = {
            'id': rating['movie']['id'],
            'title': rating['movie']['title'],
            'poster_path': rating['movie']['poster_path'],
            'backdrop_path': rating['movie']['backdrop_path']
        }
        # 해당하는 별점 배열에 영화정보 담기
        response_data['rating'][rating['score']].append(movie)

        # 만약 영화의 점수가 4점 이상이라면?
        if rating['score'] >= 4:
            for genre in rating['movie']['genres']:
                response_data['like_genre'][genre['name']] += 1

            for actor in rating['movie']['actors']:
                response_data['like_actor'][actor['name']] += 1

            for director in rating['movie']['directors']:
                response_data['like_director'][director['name']] += 1

            for keyword in rating['movie']['keywords']:
                response_data['like_keyword'][keyword['name']] += 1
        
    # 워드클라우드 분석을 위한 키워드 데이터 가공
    new_keyword_list = []
    for key, value in response_data['like_keyword'].items():
        new_keyword = {
            'name': key.upper(),
            'value': value
        }
        new_keyword_list.append(new_keyword)
    response_data['like_keyword'] = new_keyword_list

    new_genre_list = []
    # 각 항목별로 가장 선호하는 값 3개와 비율 만들기
    for key, value in sorted(response_data['like_genre'].items(), key=lambda x:x[1], reverse=True)[:3]:
        new_genre_list.append([key, round(value / len(response_data['like_genre']) * 100)])
    response_data['like_genre'] = new_genre_list
    
    new_actor_list = []
    for key, value in sorted(response_data['like_actor'].items(), key=lambda x:x[1], reverse=True)[:3]:
        new_actor_list.append([key, round(value / len(response_data['like_actor']) * 100)])
    response_data['like_actor'] = new_actor_list
    
    new_director_list = []
    for key, value in sorted(response_data['like_director'].items(), key=lambda x:x[1], reverse=True)[:3]:
        new_director_list.append([key, round(value / len(response_data['like_director']) * 100)])
    response_data['like_director'] = new_director_list

    return JsonResponse(response_data)
