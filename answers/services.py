from django.db import transaction
from django.db.models import F
from .models import Answer
from questions.models import Questions


class AnswerService:

    @staticmethod
    @transaction.atomic
    def create_answer(*, author, question, body):
        answer = Answer.objects.create(author=author, question=question, body=body)
        Questions.objects.filter(id=question.id).update(answers_count=F("answers_count") + 1)
        return answer

    @staticmethod
    @transaction.atomic
    def delete_answer(*, answer):
        question_id = answer.question.id
        answer.delete()
        Questions.objects.filter(id=question_id).update(answers_count=F("answers_count") - 1)
