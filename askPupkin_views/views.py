from django.shortcuts import render
from askPupkin_models.models import *
from askPupkin_models.accessors import *

def index(request):
    page, tags, is_hot = Question.objects.get_page(request)
    path = request.get_full_path()
    pagination = PaginationAccessor(page)
    context = {
        "questions" : page.content,
        "pagination" : pagination,
        "isHot" : is_hot,
        "tags" : tags,
        "path" : path
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

def registration(request):
    return render(request, 'registration/registration.html')

def err_handler404(request, *args, **argv):
    return render(request, 'err_handler404.html')

