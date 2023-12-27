from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from askPupkin_views.accessors import *
from askPupkin_views.forms.login_form import LoginForm
from askPupkin_views.forms.reqistartion_form import RegistrationForm
from askPupkin_views.forms.add_question_form import AddQuestionForm
from askPupkin_views.forms.add_answer_form import AddAnswerForm

def index(request):
    questions = Question.objects.filter_tags(request).order_by_param(request)
    page = questions.get_page(request)
    context = { 'context' : QuestionsAccessors(page, questions) }
    return render(request, 'index.html', context=context)

def question_page(request, question_id):
    form = AddAnswerForm(request.POST or None)
    answer_created = form.create_answer(request, question_id)
    form = AddAnswerForm()
    question = Question.objects.get(pk=question_id)
    page = Answer.objects.get_page(request, question_id, answer_created)
    context = { 'context' : AnswersAccessor(page, question), 'form' : form }
    return render(request, 'question_page.html', context=context)

@login_required(login_url='/auth/login/')
def ask(request):
    form = AddQuestionForm(request.POST or None)
    question_id = form.add_question(request)
    if question_id:
        return HttpResponseRedirect(f'/question/{question_id}/')
    return render(request, 'ask.html', {'form' : form, 'context' : { 'user' : request.user}})

@login_required(login_url='/auth/login/')
def settings(request, user_id):
    return render(request, 'settings.html')

def registration(request):
    form = RegistrationForm(request.POST or None, request.FILES or None)
    if form.check_creation(request):
        return HttpResponseRedirect("/")
    return render(request, 'auth/registration.html', {'form' : form, 'context' : { 'user' : request.user}})

def login(request):
    next = request.GET.get("next", "/")
    form = LoginForm(request.POST or None)
    if form.check_auth(request):
        return HttpResponseRedirect(next) 
    return render(request, 'auth/login.html', {"form" : form, 'context' : { 'user' : request.user}})

def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/') 


