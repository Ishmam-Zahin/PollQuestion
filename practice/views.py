from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Question, Choice

# Create your views here.
def home(request):
    questions = Question.objects.all()
    context = {
        "questions": questions
    }
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))

def sumbmitted(request):
    questions = Question.objects.all()

    for q in questions:
        q.participants += 1
        x = str(q.id)
        y = request.POST[x]
        y=int(y)
        choice = q.choice_set.get(id = y)
        choice.votes += 1
        choice.percentage = ((choice.votes)*100)/q.participants
        choice.save()
        q.save()

    return HttpResponse("your answer has been successfully submitted!")

def result(request):
    questions = Question.objects.all()
    totalParticipants = Question.objects.all()[0].participants
    context = {
        "questions": questions,
        "totalParticipants": totalParticipants
    }
    template = loader.get_template("result.html")
    return HttpResponse(template.render(context, request))