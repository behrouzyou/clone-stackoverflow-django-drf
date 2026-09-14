from django.urls import path
from . import api_views


app_name = "answers"
urlpatterns = [
    path('<uuid:question_id>/', api_views.AnswersListView.as_view()),
    path("create/<uuid:question_id>/", api_views.CreateAnswerView.as_view()),
    path("delete/<uuid:answer_id>/", api_views.DeleteAnswerView.as_view()),
]