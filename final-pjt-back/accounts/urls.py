from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
   path('<int:user_id>/rated/', views.user_rated_list), # 영화 리스트
]
