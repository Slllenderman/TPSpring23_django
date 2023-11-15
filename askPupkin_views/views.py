from django.shortcuts import render
from askPupkin_views.accessors import *

def index(request):
    context = { 'context' : QuestionsAccessors(request) }
    return render(request, 'index.html', context=context)

def question_page(request, question_id):
    context = { 'context' : AnswersAccessor(request, question_id) }
    return render(request, 'questions_page.html', context=context)

def ask(request):
    return render(request, 'ask.html')

def settings(request, user_id):
    return render(request, 'settings.html')

def registration(request):
    return render(request, 'registration/registration.html')

def err_handler404(request, *args, **argv):
    return render(request, 'err_handler404.html')

