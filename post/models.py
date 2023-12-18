from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
