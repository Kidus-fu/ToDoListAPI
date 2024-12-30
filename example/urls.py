# example/urls.py
from django.urls import path

from example.views import index, HelloView


urlpatterns = [
    path('app/', index),
    path('', HelloView.as_view()),
]