from rest_framework import serializers

from .models import List
from django.contrib.auth.models import User

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"
    def create(self,validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        print(validated_data)
        print(user)
        return List.objects.create(**validated_data)
class SingupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email']
        extra_kwargs = {'password':{'write_only':True,'required':True}}
    def create(self,validated_data):
        user = User.objects.create_user({
            'username':validated_data['username'],
            'email':validated_data['email']
        })
        user.set_password(validated_data['password'])
        return user