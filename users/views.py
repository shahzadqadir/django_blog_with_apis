from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model

from users.forms import CustomUserCreationForm

class UserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "users/registration.html"
    success_url = reverse_lazy("login")

    # fields = ("email", "username", "password")