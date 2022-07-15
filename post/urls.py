from django.urls import path

from .views import *

app_name = 'post'
urlpatterns = [
    path('', home, name='home'),
    path('posts/', posts, name='posts'),
    path('posts/<int:pk>', detail, name='post_detail'),
    path('posts/<int:pk>/reply', commentReply, name='comment_reply'),
    path('search', search, name='search'),
    path('categories/<int:pk>', category_posts, name='category_posts'),
]