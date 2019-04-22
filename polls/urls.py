from django.urls import path
from . import views

urlpatterns = [
    path('poll', views.PollsList.as_view(), name='polls'),
    path('poll/finish', views.FinishPoll.as_view(), name='finish_poll'),
    path('poll/<int:pk>', views.PollDetail.as_view(), name='poll_detail'),
    path('poll/<int:pk>/result', views.PollResult.as_view(), name='poll_result'),
    path('poll/<int:pk>/question', views.QuestionList.as_view(), name='questions'),
    path('question/<int:pk>', views.QuestionDetail.as_view(), name='question_detail'),
    path('question/<int:pk>/answer', views.AnswerForQuestion.as_view(), name='answers_for_question'),
    path('answer', views.AnswerList.as_view(), name='answers'),
    path('answer/<int:pk>', views.AnswerDetail.as_view(), name='answer_detail')
]