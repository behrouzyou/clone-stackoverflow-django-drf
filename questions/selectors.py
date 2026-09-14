from .models import Questions


def get_all_questions():
    return Question.objects.all()

def get_question_by_id(*,qid):
    return Question.objects.get(id=qid)