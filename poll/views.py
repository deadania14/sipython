from django.shortcuts import render
from .models import Question

def index(request):
    context={}
    questions_query = Question.objects.all()
    context['questions'] = questions_query
    return render(request, 'poll/index.html',context) #render biar index muncul
def helpme(request):
    context={}
    return render(request, 'poll/helpme.html',context) #biar muncul
def detail_question(request, question_id):
    context={}
    question= Question.objects.get(id=question_id)
    context['question'] = question
    return render(request, 'poll/detail_question.html',context) #biar muncul
