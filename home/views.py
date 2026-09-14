from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import  IsAdminUser


class Home(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({"message":"Hello user..!"})
