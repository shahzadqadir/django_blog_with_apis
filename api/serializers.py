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






