from .models import Answer


def get_answers_for_question(*, question):
    return Answer.objects.filter(question=question)


def get_answer_by_id(*, answer_id):
    return Answer.objects.get(id=answer_id)
