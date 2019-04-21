from django.urls import path
from . import views

urlpatterns = [
    path('', views.PollsList.as_view(), name='polls'),
]