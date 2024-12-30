# example/urls.py
from django.urls import path

from example.views import index, HelloView


urlpatterns = [
    path('', index),
    path('hello/', HelloView.as_view()),
]