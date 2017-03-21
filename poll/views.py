from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

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
def vote(request):
    context={}
    choice_id = request.POST['choice']
    selected_choice = Choice.objects.get(id=int(choice_id))
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse ('poll:results', args =(selected_choice.question.id,)))
def results(request, question_id):
    context={}
    question = Question.objects.get(pk=question_id)
    return render(request, 'poll/results.html', {'question':question}) #render biar index muncul
