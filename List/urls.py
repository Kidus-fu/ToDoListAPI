from django.urls import path
"""
URL configuration for the ToDoListAPI application.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
Routes:
    - 'list/<int:pk>': Retrieves details of a specific list item by its primary key (pk).
    - 'list/': Retrieves a list of all list items.
    - 'signup/': Endpoint for user signup.
    - 'token/': Endpoint to obtain a new JWT token.
    - 'token/refresh/': Endpoint to refresh an existing JWT token.
Views:
    - ListView: Handles the retrieval of list items.
    - SingupView: Handles user signup.
    - TokenObtainPairView: Handles obtaining JWT tokens.
    - TokenRefreshView: Handles refreshing JWT tokens.
"""

from .views import ListView, SingupView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('list/<int:pk>', ListView.as_view(), name='listDetials'),
    path('list/', ListView.as_view(), name='list'),
    path('signup/', SingupView.as_view(), name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
