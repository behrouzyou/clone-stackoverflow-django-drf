from rest_framework.views import APIView
from rest_framework.response import Response
from questions.selectors import get_question_by_id
from .selectors import get_answers_for_question, get_answer_by_id
from .serializers import AnswersListSerializer, AnswerCreateSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsOwnerOrReadOnly
from .services import AnswerService
from rest_framework import status


class AnswersListView(APIView):
    def get(self, request, question_id):
        question = get_question_by_id(qid=question_id)
        answers = get_answers_for_question(question=question)
        serializer = AnswersListSerializer(instance=answers, many=True)
        return Response(serializer.data)


class CreateAnswerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, question_id):
        serializer = AnswerCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = get_question_by_id(qid=question_id)
        answer =  AnswerService.create_answer(author=request.user, question=question, body=serializer.validated_data["body"])
        return Response(AnswersListSerializer(answer).data, status=status.HTTP_201_CREATED)


class DeleteAnswerView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def delete(self, request, answer_id):
        answer = get_answer_by_id(answer_id=answer_id)
        self.check_object_permissions(request, answer)
        AnswerService.delete_answer(answer=answer)
        return Response(status=status.HTTP_204_NO_CONTENT)
