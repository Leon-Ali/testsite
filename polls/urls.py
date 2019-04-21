from django.urls import path
from . import views

urlpatterns = [
    path('poll', views.PollsList.as_view(), name='polls'),
    path('poll/<int:pk>', views.PollDetail.as_view(), name='poll_detail')
]