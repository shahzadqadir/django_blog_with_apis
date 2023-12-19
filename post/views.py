from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from post.models import Post

class PostsView(generic.ListView):
    model = Post
    template_name = "pages/posts.html"
    context_object_name = "posts"


@login_required
def post(request, pk):
    if request.method == "GET":
        is_author = False
        post = Post.objects.get(id=pk)
        if request.user == post.author:
            is_author = True
        return render(request, 'pages/post_detail.html', {'post': post, 'is_author': is_author})


@login_required
def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    if request.user == post.author:
        post.delete()
        return redirect(reverse("posts"))


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = "pages/post_update.html"
    fields = ("title", "text")

# class PostDetailView(LoginRequiredMixin, generic.DetailView):
#     model = Post
#     template_name = "pages/post_detail.html"
#     context_object_name = "post"
#     login_url = reverse_lazy("login")



