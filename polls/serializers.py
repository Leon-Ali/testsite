from .models import Poll, Question, Answer, FinishedPoll
from rest_framework import serializers


class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ('id', 'name')


class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        for i in self._choices:
            if obj in i:
                return i[-1]


    def to_internal_value(self, data):
        for i in self._choices:
            if data in i:
                return i[0]


class QuestionSerializer(serializers.ModelSerializer):
    group = ChoicesField(choices=Question.GROUP_CHOICES, required=True)

    class Meta:
        model = Question
        fields = ('id', 'header', 'order', 'group')


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'text', 'order')


class FinishedPollSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinishedPoll
        fields = ('id', 'user', 'answer')
