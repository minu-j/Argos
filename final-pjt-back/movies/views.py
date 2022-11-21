import random

from django.db.models import Count
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

from django.http import JsonResponse

User = get_user_model()

########################### 영화 ######################################

# 전체 영화 리스트 호출
@api_view(['GET'])
def all_movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = AllMovieListSerializer(movies, many=True)
    return Response(serializer.data)

# 단일 영화 호출
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

# 평가용 랜덤 영화 불러오기
@api_view(['GET'])
def get_movie_random(request):
    movie = get_list_or_404(Movie)
    serializer = MovieSearchSerializer(movie, many=True)
    response_data = []
    
    num_range = list(range(0, len(serializer.data)))
    
    # 랜덤으로 표시하도록 데이터 섞기
    for i in random.sample(num_range, 24):
        response_data.append(serializer.data[i])

    return JsonResponse({ 'data': response_data })


########################### 장르 ######################################

# 전체 장르 리스트 호출
@api_view(['GET'])
def genre_list(request):
    genres = get_list_or_404(Genre)
    serializer = GenreMovieSerializer(genres, many=True)
    return Response(serializer.data)

# 단일 장르 호출
@api_view(['GET'])
def genre_detail(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreMovieSerializer(genre)
    return Response(serializer.data)


########################### 배우 ######################################

# 전체 배우 리스트 호출
@api_view(['GET'])
def actor_list(request):
    actors = get_list_or_404(Actor)
    serializer = ActorMovieSerializer(actors, many=True)
    return Response(serializer.data)

# 단일 배우 호출
@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorMovieSerializer(actor)
    return Response(serializer.data)


########################### 감독 ######################################

# 전체 감독 리스트 호출
@api_view(['GET'])
def director_list(request):
    directors = get_list_or_404(Director)
    serializer = DirectorMovieSerializer(directors, many=True)
    return Response(serializer.data)

# 단일 감독 호출
@api_view(['GET'])
def director_detail(request, director_pk):
    director = get_object_or_404(Director, pk=director_pk)
    serializer = DirectorMovieSerializer(director)
    return Response(serializer.data)


########################### 키워드 ######################################

# 전체 키워드 리스트 호출
@api_view(['GET'])
def keyword_list(request):
    keywords = get_list_or_404(Keyword)
    serializer = KeywordMovieSerializer(keywords, many=True)
    return Response(serializer.data)

# 단일 키워드 호출
@api_view(['GET'])
def keyword_detail(request, keyword_pk):
    keyword = get_object_or_404(Keyword, pk=keyword_pk)
    serializer = KeywordMovieSerializer(keyword)
    return Response(serializer.data)


########################### 예고편 ######################################

# 전체 예고편 리스트 호출
@api_view(['GET'])
def video_list(request):
    videos = get_list_or_404(Video)
    serializer = VideoMovieSerializer(videos, many=True)
    return Response(serializer.data)


########################### 공급자 ######################################

# 전체 공급자 리스트 호출
@api_view(['GET'])
def provider_list(request):
    providers = get_list_or_404(Provider)
    serializer = ProviderMovieSerializer(providers, many=True)
    return Response(serializer.data)

# 단일 공급자 호출
@api_view(['GET'])
def provider_detail(request, provider_pk):
    provider = get_object_or_404(Provider, pk=provider_pk)
    serializer = ProviderMovieSerializer(provider)
    return Response(serializer.data)


########################### 별점 ######################################

# 영화에 별점 주기
@api_view(['POST'])
def rating_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 별점 조회, 삭제
@api_view(['GET', 'DELETE'])
def rating_detail(request, rating_pk):
    rating = get_object_or_404(Rating, pk=rating_pk)
    
    if request.method == 'GET':
        serializer = RatingSerializer(rating)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        rating.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

########################### 리뷰 ######################################

# 영화에 리뷰 쓰기
@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 리뷰 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

########################### 댓글 ######################################

# 리뷰에 댓글 쓰기
@api_view(['POST'])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# 댓글 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)