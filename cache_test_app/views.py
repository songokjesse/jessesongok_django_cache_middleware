from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.core.cache import cache
from .models import Post
from .serializers import  PostSerializer
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
# Create your views here.

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(['GET'])
def view_cached_product(request):
    if 'product' in cache:
        # get results from cache
        products = cache.get('product')
        return Response(products, status=status.HTTP_201_CREATED)

    else:
        posts = Post.objects.all()
        results = [product.to_json() for product in posts]
        # store data in cache
        cache.set(posts, results, timeout=CACHE_TTL)
        return Response(results, status=status.HTTP_201_CREATED)