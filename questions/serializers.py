from rest_framework import serializers
from .models import Questions

class QuestionListSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    body = serializers.CharField()
    views_count = serializers.IntegerField()

class QuestionDetailSerializer(serializers.ModelSerializer):
    author_username =serializers.CharField(source='author.username')
    class Meta:
        model = Questions
        exclude =['author']

class QuestionCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()

class QuestionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields=['title','body']