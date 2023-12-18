from rest_framework import generics
from django.contrib.auth import get_user_model
from post.models import Post
from api.serializers import AuthorSerializer, PostSerializer
from api.permissions import PostPermissions

Author = get_user_model()


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [PostPermissions, ]

    # def destroy(self, value):
    #     print("delete was tried!")

