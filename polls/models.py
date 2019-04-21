from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    name = models.CharField(max_length=200, default='untitled')



class Question(models.Model):
    MOVIES = 'MV'
    GAMES = 'GA'
    BOOKS = 'BO'

    GROUP_CHOICES = (
        (MOVIES, 'movies'),
        (GAMES, 'games'),
        (BOOKS, 'books')
    )

    header = models.CharField(max_length=200)
    order = models.IntegerField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    group = models.CharField(max_length=2, choices=GROUP_CHOICES)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    order = models.IntegerField()


class FinishedPoll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

