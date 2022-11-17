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