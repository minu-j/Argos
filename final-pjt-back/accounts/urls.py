from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
   path('delete/', views.user_delete), # 회원탈퇴
]
