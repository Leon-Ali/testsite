from django.contrib import admin
from .models import Question, Poll, Answer, FinishedPoll

admin.site.register(Question)
admin.site.register(Poll)
admin.site.register(Answer)
admin.site.register(FinishedPoll)
