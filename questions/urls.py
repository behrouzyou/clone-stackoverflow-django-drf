from django.urls import path

from . import views, api_views

app_name = 'questions'
urlpatterns = [
    path('',api_views.AllQuestionsView.as_view()),
    path('<uuid:id>/',api_views.QuestionDetailView.as_view()),
    path('create/',api_views.QuestionCreateView.as_view()),
    path('delete/<uuid:qid>/',api_views.QuestionDeleteView.as_view()),
    path('update/<uuid:qid>/',api_views.QuestionUpdateView.as_view()),
    path('accept/<uuid:question_id>/<uuid:answer_id>/',api_views.AcceptAnswerView.as_view()),

]