from django.urls import path
from . import  views

app_name = 'posts' # app_name - specified for django

urlpatterns = [
    path('', views.posts, name = 'posts'),
    path('<int:postId>/', views.specifiedPost, name = 'specifiedPost'),
    path('<int:postId>/leaveComment/', views.leaveComment, name = 'leaveComment'),
]