from polls.models import Poll, Question, Answer, FinishedPoll
from polls.serializers import PollSerializer, QuestionSerializer, AnswerSerializer, FinishedPollSerializer
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
import json

class PollsList(generics.ListCreateAPIView):
    """Create the Poll and get all the Polls"""
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, Update and Destroy a poll by id"""
    queryset = Poll.objects.all()
    serializer_class = PollSerializer




class QuestionList(APIView):
    """Creates the and retrieves Questions"""


    def post(self, request, pk, format='json'):
        poll = Poll.objects.get(id=pk)
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save(poll=poll)
            if question:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        poll = Poll.objects.get(id=pk)
        question = Question.objects.filter(poll=poll).all()
        serializer = QuestionSerializer(question, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, Update and Destroy an question by id"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer




class AnswerList(generics.ListCreateAPIView):
    """Creates the and retrieves Answers"""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer



class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieves, Updates and Destroys an answer by id"""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerForQuestion(APIView):
    """Creates the and retrieves Answers for specific question"""

    def get(self, request, pk):
        question = Question.objects.get(id=pk)
        answers = Answer.objects.filter(question=question).all()
        serializer = AnswerSerializer(answers, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FinishPoll(APIView):

    def post(self, request, format='json'):
        user = User.objects.get(pk=request.user.id)
        answer = Answer.objects.get(pk=request.data['answer'])
        data = {'user':user.id, 'answer':answer.id}
        serializer = FinishedPollSerializer(data=data)
        if serializer.is_valid():
            poll = serializer.save()
            if poll:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PollResult(APIView):

    def get(self, request, pk):
        polls = FinishedPoll.objects.all()
        result = dict()
        for i in polls:
            if i.answer.question.poll.id == pk:
                result[i.answer.question.header] = i.answer.text
        if result:
            data = json.dumps(result)
            return Response(data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)










