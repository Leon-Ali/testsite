from polls.models import Poll, Question, Answer, FinishedPoll
from polls.serializers import PollSerializer, QuestionSerializer, AnswerSerializer, FinishedPollSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

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
