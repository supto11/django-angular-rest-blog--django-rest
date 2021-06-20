from django.urls import path
from .views import api_overview, get_posts

urlpatterns = [
    path('', api_overview),
    path('posts/', get_posts)
]