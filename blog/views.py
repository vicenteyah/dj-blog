from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

# Create your views here.
from .models import Post
from .serializers import PostSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

