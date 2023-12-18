# Blog
Features Implemented
## APIs using DRF

### Routes
```
urlpatterns = [
    path("posts/", PostListCreateView.as_view(), name="api_posts"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="api_post_detail"),
    path("authors/", AuthorListCreateView.as_view(), name="api_authors"),
    path("auth-token/", views.obtain_auth_token , name="auth_token"),
]
``````
### Views

```
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
```

### Serializers

```
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone
from post.models import Post

CustomUser = get_user_model()

class AuthorSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6, max_length=20, write_only=True)
    is_superuser = serializers.BooleanField()

    def validate_username(self, value):
        if len(CustomUser.objects.filter(username=value)) > 0:
            raise serializers.ValidationError("username already exist")
        return value

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance



class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField(max_length=255, read_only=True)
    text = serializers.CharField(max_length=255)
    date_posted = serializers.DateTimeField(default=timezone.now(), required=False)

    def validate_author(self, value):
        author = CustomUser.objects.filter(username=value).first()
        if not author:
            raise serializers.ValidationError("Author does not exist. Create author first!")
        return value

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            author = request.user
        # author = CustomUser.objects.filter(username=self.request.user).first()
        if author:
            return Post.objects.create(author=author, text=validated_data['text'])
        return None
```

### Authentication
### Authorization
### Permission Classes