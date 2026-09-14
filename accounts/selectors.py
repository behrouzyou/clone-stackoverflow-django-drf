from .models import *

def get_user_by_id(user_id):
    return User.objects.filter(id=user_id).first()
def get_user_by_mail(email):
    return User.objects.filter(email=email).first()

def get_all_user():
    return User.objects.all()