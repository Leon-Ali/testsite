from polls.models import Poll
from polls.serializers import PollSerializer
from rest_framework import generics

class PollsList(generics.ListCreateAPIView):
    """Create the Poll and get all the Polls"""
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, Update and Destroy a poll by id"""
    queryset = Poll.objects.all()
    serializer_class = PollSerializer




