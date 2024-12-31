from django.urls import path

from .views import ListView, SingupView

urlpatterns = [
    path('list/', ListView.as_view(), name='list'),
    path('signup/', SingupView.as_view(), name='signup'),
]
