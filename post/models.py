from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="")
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self, *args, **kwargs):
        return reverse("post_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.text
