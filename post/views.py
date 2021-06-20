from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'All Posts': 'posts',
        'Create': 'post/create',
        'Update': 'post/<str:pk>',
        'Delete': 'post/<str:pk>',
    }
    return Response(api_urls)
