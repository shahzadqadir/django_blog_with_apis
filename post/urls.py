from django.urls import path
from post.views import PostsView, post, post_delete, PostUpdateView



urlpatterns = [
    path("", PostsView.as_view(), name="posts"),
    path("<int:pk>/", post, name="post_detail"),
    path("<int:pk>/delete/", post_delete, name="post_delete"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
]