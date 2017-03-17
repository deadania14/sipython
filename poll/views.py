from django.shortcuts import render

def index(request):
    context={}
    return render(request, 'poll/index.html',context) #biar muncul
def helpme(request):
    context={}
    return render(request, 'poll/helpme.html',context) #biar muncul
