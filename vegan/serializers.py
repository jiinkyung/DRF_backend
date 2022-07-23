from dataclasses import fields
from rest_framework import serializers
from .models import Vegan, Comment
from django.contrib.auth.models import User

class VeganSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegan
        fields = ('id', 'title', 'author', 'description')

class VeganDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegan
        fields = ('id', 'title', 'author', 'description', 'created')

class VeganCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegan
        fields = ('title','author', 'description')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'author', 'date', 'post')

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')