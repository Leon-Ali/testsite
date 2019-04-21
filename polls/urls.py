from django.urls import path
from . import views

urlpatterns = [
    path('poll', views.PollsList.as_view(), name='polls'),
    path('poll/<int:pk>', views.PollDetail.as_view(), name='poll_detail'),
    path('poll/<int:pk>/question', views.QuestionList.as_view(), name='question'),
    path('question/<int:pk>', views.QuestionDetail.as_view())
]