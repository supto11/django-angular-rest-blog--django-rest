from django.urls import path
from .views import api_overview, get_posts, create_post

urlpatterns = [
    path('', api_overview),
    path('posts/', get_posts),
    path('posts/create', create_post),
]