from django.conf import settings
from django.db import models

from core.models import BaseModel
from questions.models import Questions


class Answer(BaseModel):
    question = models.ForeignKey(Questions,on_delete=models.CASCADE,related_name='answers')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='answers')
    body = models.TextField()
    is_accepted = models.BooleanField(default=False)
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ('-is_accepted','-score','-created')

    def __str__(self) -> str:
        return f'Answer #{self.pk}'