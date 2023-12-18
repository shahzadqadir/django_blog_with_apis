from django.urls import path, include
from rest_framework.authtoken import views
from api.views import (
    PostListCreateView, AuthorListCreateView,
    PostDetailView,
    )

urlpatterns = [
    path("posts/", PostListCreateView.as_view(), name="api_posts"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="api_post_detail"),
    path("authors/", AuthorListCreateView.as_view(), name="api_authors"),
    path("auth-token/", views.obtain_auth_token , name="auth_token"),
]