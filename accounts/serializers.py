from typing import Any

from rest_framework import serializers

from questions.serializers import QuestionListSerializer
from .models import User

class UserSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    class Meta:
        model = User
        field =['id','email','username','is_active','is_staff','date_joined','questions']

    def get_questions(self,obj):
        qs=obj.questions.all()
        return QuestionListSerializer(instance=qs,many=True).data

def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('email cant contain admin')

class UserRegisterSerializer(serializers.Serializer):
    email = serializers.CharField(required=True,validators=[clean_email])
    username = serializers.CharField(required=True)
    password =serializers.CharField(required=True,write_only=True)
    password2 =serializers.CharField(required=True,write_only=True)

    def validate_username(self,value):
        if value == 'admin':
            raise serializers.ValidationError('username cant be admin')
        return value
    def validate(self,data) :
        if data['password'] != data['password2']:
            raise serializers.ValidationError('passwords do not match')
        return data

class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField()

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()