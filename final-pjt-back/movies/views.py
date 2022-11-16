# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.shortcuts import get_object_or_404, get_list_or_404

# from .models import Movie
# from .serializers import MovieListSerializer

# from django.shortcuts import render

# # 영화 리스트
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = get_list_or_404(Movie)
#         serializer = MovieListSerializer(movies, many=True)
#         return Response(serializer.data)