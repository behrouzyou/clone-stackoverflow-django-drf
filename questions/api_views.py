from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions import IsOwnerOrReadOnly
from .selectors import get_question_by_id
from .serializers import *
from .models import *
from .services import QuestionService


class AllQuestionsView(APIView):
    def get(self,request):
        questions =Questions.objects.all()
        serialized_data=QuestionListSerializer(instance=questions,many=True)
        return Response(serialized_data.data,status=status.HTTP_200_OK)

class QuestionDetailView(APIView):
    def get(self,request,id):
        question = Questions.objects.get(id=id)
        serializer_data= QuestionDetailSerializer(instance=question)
        QuestionService.increment_views(question=question)
        return Response(serializer_data.data,status=status.HTTP_200_OK)

class QuestionCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer =QuestionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question =QuestionService.create_question(author=request.user,title=serializer.validated_data['title'],body=
                                                  serializer.validated_data['body'])
        return Response(QuestionDetailSerializer(instance=question).data)

class QuestionDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    def delete(self,request,qid):
        question =get_question_by_id(qid=qid)
        self.check_object_permissions(request,question)
        QuestionService.delete_question(question=question)
        return Response(status = status.HTTP_204_NO_CONTENT)

class QuestionUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    def patch(self,request,qid):
        question =get_question_by_id(qid=qid)
        self.check_object_permissions(request,question)
        serializer=QuestionUpdateSerializer(instance=question,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(QuestionDetailSerializer(instance=question).data)
