from rest_framework.exceptions import PermissionDenied, ValidationError

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

    @staticmethod
    @transaction.atomic
    def accept_answer(*,question,answer,accepted_by):
        if question.author.id != accepted_by.id:
            raise PermissionDenied('only owner can accepted answer')
        if answer.question.id != question.id:
            raise ValidationError('answer does not belong to question')
        if question.accepted_answer:
            raise ValidationError('question already have accepted answer')
        question.accepted_answer=answer
        question.save(updated_field=['accepted_answer'])
        answer.is_accepted=True
        answer.save(updated_fields=['is_accepted'])
        return question