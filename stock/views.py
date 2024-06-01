from django.shortcuts import render
from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import Group, Sub_Group


# Create your views here.
class GroupSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Group
        fields = ('id', 'name', 'Description', 'is_active', 'creator')


class SubGroupSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Sub_Group
        fields = ('id', 'name', 'Description', 'group', 'is_active', 'creator')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'movies')
