from django.conf import settings
from django.db import models


from core.models import BaseModel


class Questions(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='questions')
    title = models.CharField(max_length=255,db_index=True)
    body = models.TextField()
    view_count = models.PositiveIntegerField(default=0)
    answers_count = models.PositiveIntegerField(default=0)
    score = models.IntegerField(default=0)
    accepted_answer = models.OneToOneField('answers.Answer',on_delete=models.SET_NULL,null=True,blank=True,related_name='accepted_for_questions')

    class Meta:
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.title