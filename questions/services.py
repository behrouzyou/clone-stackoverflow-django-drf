from .models import *
from django.db import transaction
from django.db.models import F
class QuestionService:
    @staticmethod
    @transaction.atomic
    def create_question(*,author,title,body):
        question =Questions.objects.create(author=author,title=title,boyd=body)
        return question

    @staticmethod
    def increment_views(*,question):
        Questions.objects.filter(id=question.id).update(views_count=F('views_count') + 1)

    @staticmethod
    @transaction.atomic
    def delete_question(*,question):
        question.delete()