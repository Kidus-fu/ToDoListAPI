from django.shortcuts import render

from rest_framework import generics,mixins

from .models import List
from .serializers import ListSerializer,SingupSerializer

from rest_framework import permissions

class UserMixins():
    user_filed = "user"
    def get_queryset(self):
        print(self.request.user)
        return List.objects.filter(created_by=self.request.user)

class ListView(generics.GenericAPIView,
               UserMixins,
               mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin):
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return UserMixins.get_queryset(self)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class SingupView(generics.GenericAPIView,
                 mixins.CreateModelMixin):
    serializer_class = SingupSerializer
    queryset = List.objects.all()

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)