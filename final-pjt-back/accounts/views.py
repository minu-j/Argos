import random
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404, get_list_or_404
from collections import defaultdict

# from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from .serializers import *
from movies.serializers import *

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


################################## 영화 추천 알고리즘 ##################################

# 유저가 준 모든 평점의 영화 리스트를 기반으로 취향을 계산하여 반환
@api_view(['GET'])
def get_user_recommend(request, user_pk):
    ratings = get_list_or_404(Rating, user_id=user_pk)
    serializer = RatingListSerializers(ratings, many=True)

    response_data = { 'data': [] }

    # 반환할 객체
    recommend_data = {
        ### 4점 이상 준 영화와 매칭되는 특징을 정리
        # 각 영화를 순회하면서 별점이 높은 특징을 딕셔너리로 만들기
        'like_genre': defaultdict(int), # 좋아하는 장르
        'like_actor': defaultdict(int), # 좋아하는 배우
        'like_director': defaultdict(int), # 좋아하는 감독
        'like_keyword': defaultdict(int) # 좋아하는 키워드    
    }
    
    # 홈 화면에 표시할 접두사 : ~ 판타지 장르 영화
    prefix = ['선호하는', '회원님이 좋아하는', '좋아하는', '재밌게 본 영화의', '오늘 저녁엔', 'ARGOS가 보장하는', '눈이 즐거울', '기억에 남을만 한', '대리만족할 수 있는', '한번 보고 두번도 볼', '인생영화가 될 수 있는']

    for rating in serializer.data:

        # 만약 영화의 점수가 4점 이상이라면?
        if rating['score'] >= 4:
            for genre in rating['movie']['genres']:
                recommend_data['like_genre'][genre['id']] += 1

            for actor in rating['movie']['actors']:
                recommend_data['like_actor'][actor['id']] += 1

            for director in rating['movie']['directors']:
                recommend_data['like_director'][director['id']] += 1

            for keyword in rating['movie']['keywords']:
                recommend_data['like_keyword'][keyword['id']] += 1

    

    # 각 항목별로 가장 선호하는 값 4개중에 랜덤으로 2개 뽑기
    genre_list = [] # 장르
    for key, value in sorted(recommend_data['like_genre'].items(), key=lambda x:x[1], reverse=True)[:4]: # 선호하는 4개 값
        genre_list.append(key)
    if len(genre_list) > 2:
        genre_list = random.sample(genre_list, 3) # 랜덤으로 2개 뽑기
    else:
        genre_list = random.sample(genre_list, 1)
    for genre_id in genre_list:
        genre = get_object_or_404(Genre, pk=genre_id) # 해당 id에 맞는 영화 가져오기
        serializer = GenreMovieSerializer(genre)
        select_len = 10 # 10개 영화를 기본으로 뽑는데, 영화가 10개가 안되면 길이에 맞게 선정
        if len(serializer.data["movie_set"]) < 10:
            select_len = len(serializer.data["movie_set"])
        if len(serializer.data["movie_set"]) >= 5:
            genre_recommend = {
                'prefix': random.choice(prefix),
                'category': '장르',
                'name': serializer.data["name"],
                'movies': random.sample(serializer.data["movie_set"], select_len)
            }
            response_data['data'].append(genre_recommend)

    actor_list = [] # 배우
    for key, value in sorted(recommend_data['like_actor'].items(), key=lambda x:x[1], reverse=True)[:4]: # 선호하는 4개 값
        actor_list.append(key)
    if len(actor_list) > 2:
        actor_list = random.sample(actor_list, 3) # 랜덤으로 2개 뽑기
    else:
        actor_list = random.sample(actor_list, 1)
    for actor_id in actor_list:
        actor = get_object_or_404(Actor, pk=actor_id) # 해당 id에 맞는 영화 가져오기
        serializer = ActorMovieSerializer(actor)
        select_len = 10 # 10개 영화를 기본으로 뽑는데, 영화가 10개가 안되면 길이에 맞게 선정
        if len(serializer.data["movie_set"]) < 10:
            select_len = len(serializer.data["movie_set"])
        if len(serializer.data["movie_set"]) >= 5:
            actor_recommend = {
                'prefix': random.choice(prefix),
                'category': '배우',
                'name': serializer.data["name"],
                'movies': random.sample(serializer.data["movie_set"], select_len)
            }
            response_data['data'].append(actor_recommend)

    director_list = [] # 감독
    for key, value in sorted(recommend_data['like_director'].items(), key=lambda x:x[1], reverse=True)[:4]: # 선호하는 4개 값
        director_list.append(key)
    if len(director_list) > 2:
        director_list = random.sample(director_list, 3) # 랜덤으로 2개 뽑기
    else:
        director_list = random.sample(director_list, 1)
    for director_id in director_list:
        director = get_object_or_404(Director, pk=director_id) # 해당 id에 맞는 영화 가져오기
        serializer = DirectorMovieSerializer(director)
        select_len = 10 # 10개 영화를 기본으로 뽑는데, 영화가 10개가 안되면 길이에 맞게 선정
        if len(serializer.data["movie_set"]) < 10:
            select_len = len(serializer.data["movie_set"])
        if len(serializer.data["movie_set"]) >= 5:
            director_recommend = {
                'prefix': random.choice(prefix),
                'category': '감독',
                'name': serializer.data["name"],
                'movies': random.sample(serializer.data["movie_set"], select_len)
            }
            response_data['data'].append(director_recommend)

    keyword_list = [] # 키워드
    for key, value in sorted(recommend_data['like_keyword'].items(), key=lambda x:x[1], reverse=True)[:4]: # 선호하는 4개 값
        keyword_list.append(key)
    if len(keyword_list) > 2:
        keyword_list = random.sample(keyword_list, 3) # 랜덤으로 2개 뽑기
    else:
        keyword_list = random.sample(keyword_list, 1)
    for keyword_id in keyword_list:
        keyword = get_object_or_404(Keyword, pk=keyword_id) # 해당 id에 맞는 영화 가져오기
        serializer = KeywordMovieSerializer(keyword)
        select_len = 10 # 10개 영화를 기본으로 뽑는데, 영화가 10개가 안되면 길이에 맞게 선정
        if len(serializer.data["movie_set"]) < 10:
            select_len = len(serializer.data["movie_set"])
        if len(serializer.data["movie_set"]) >= 5:
            keyword_recommend = {
                'prefix': random.choice(prefix),
                'category': '키워드',
                'name': serializer.data["name"],
                'movies': random.sample(serializer.data["movie_set"], select_len)
            }
            response_data['data'].append(keyword_recommend)

    # 랜덤으로 표시하도록 데이터 섞기
    random.shuffle(response_data['data'])

    return JsonResponse(response_data)


################################## 사용자 영화 취향 파악 알고리즘 ##################################

# 유저가 준 모든 평점의 영화 리스트를 기반으로 취향을 계산하여 반환
@api_view(['GET'])
def get_user_analysis(request, username):
    user = get_object_or_404(User, username=username)
    user_pk = user.id
    ratings = get_list_or_404(Rating, user_id=user_pk)
    serializer = RatingListSerializers(ratings, many=True)

    # 반환할 객체
    response_data = {
        'rating': {
            5: [],
            4: [],
            3: [],
            2: [],
            1: []
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

    # 각 항목별로 가장 선호하는 값 3개와 비율 만들기
    new_genre_list = []
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


#########################################################################

# 회원 탈퇴
@api_view(['POST'])
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return Response(request)


# 팔로우
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def follow(request, username):

    # 내가 팔로잉한 사람인지 확인
    if request.method == 'GET':
        person = get_object_or_404(get_user_model(), username=username)
        user = request.user
        
        if person != user:
            isFollow = False
            # 내가 (request.user) 그 사람의 팔로워 목록에 있다면
            if person.followers.filter(pk=user.pk).exists():
                isFollow = True
            return JsonResponse({'isFollow': isFollow})
    
    elif request.method == 'POST':
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
            }
            return JsonResponse(follow_status)
        

# 팔로우 데이터 가져오기
@api_view(['GET'])
def get_user_follow(request, username):
    user = get_list_or_404(User, username=username)
    serializer = UserFollowListSerializers(user, many=True)
    return Response(serializer.data)
    
############################ 유저가 작성한 리뷰, 코멘트 조회 #############################

@api_view(['GET'])
def get_user_review(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserInfoSerializers(user)
    user_id = serializer.data['id']
    
    review = get_list_or_404(Review, user_id=user_id)
    serializer = UserReviewSerializers(review, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_comment(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserInfoSerializers(user)
    user_id = serializer.data['id']
    
    comment = get_list_or_404(Comment, user_id=user_id)
    serializer = UserCommentSerializers(comment, many=True)
    return Response(serializer.data)