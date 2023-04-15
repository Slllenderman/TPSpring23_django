from django.shortcuts import render
from .models import *

def index(request):
    page = Question.objects.get_page(request)
    return render(request, 'index.html', context={ 'page' : page })

def ask(request):
    return render(request, 'ask.html')

def question(request, question_id):
    return render(request, 'question.html')

def settings(request, user_id):
    return render(request, 'settings.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def err_handler404(request, *args, **argv):
    return render(request, 'err_handler404.html')

