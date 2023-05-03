from django.shortcuts import render
from .models import *
from .accessors import *

def index(request):
    page = Question.objects.get_page(request)
    pagination = PaginationAccessor(page)
    context = {
        "questions" : page.content,
        "pagination" : pagination
    }
    return render(request, 'index.html', context=context)

def hot(request):
    page = Question.objects.get_page(request, order_by_rating=True)
    pagination = PaginationAccessor(page)
    context = {
        "pagination" : pagination,
        "questions" : page.content,
        "isHot" : True
    }
    return render(request, 'index.html', context=context)

def tag_question(request, tag_name):
    page = Question.objects.get_page(request, order_by_rating=True, tag=tag_name)
    pagination = PaginationAccessor(page)
    context = {
        "pagination" : pagination,
        "questions" : page.content,
        "isHot" : True,
        "tagName" : tag_name
    }
    return render(request, 'index.html', context=context)

def question(request, question_id):
    question = Question.objects.get(pk=question_id)
    page = Answer.objects.get_page(request, question_id)
    pagination = PaginationAccessor(page)
    context = {
        "pagination" : pagination,
        "question" : question,
        "answers" : page.content
    }
    return render(request, 'question.html', context=context)

def ask(request):
    return render(request, 'ask.html')

def settings(request, user_id):
    return render(request, 'settings.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def err_handler404(request, *args, **argv):
    return render(request, 'err_handler404.html')

