from django.shortcuts import render
from askPupkin_views.accessors import *

def index(request):
    questions = Question.objects.filter_tags(request).order_by_param(request)
    page = questions.get_page(request)
    context = { 'context' : QuestionsAccessors(page, questions) }
    return render(request, 'index.html', context=context)

def question_page(request, question_id):
    context = { 'context' : AnswersAccessor(request, question_id) }
    return render(request, 'question_page.html', context=context)

def ask(request):
    return render(request, 'ask.html')

def settings(request, user_id):
    return render(request, 'settings.html')

def registration(request):
    return render(request, 'registration/registration.html')


