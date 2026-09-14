from rest_framework import serializers
from .models import Answer
from core.fields import QuestionTitleViewCountField


class AnswersListSerializer(serializers.ModelSerializer):
    author_email = serializers.CharField(source="author.email", read_only=True)
    question = QuestionTitleViewCountField(read_only=True)

    class Meta:
        model = Answer
        fields = ("id", "body", "score", "is_accepted", "created", "author_email", "question")


class AnswerCreateSerializer(serializers.Serializer):
    body = serializers.CharField()
