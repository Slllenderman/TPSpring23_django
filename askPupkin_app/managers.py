from django.db import models
from .accessors import PageAccessor
from django.core.paginator import Paginator


DEFAULT_PAGE = 1
PAGINATION_STEP = 10

def get_page(queryset, page_num, step=PAGINATION_STEP):
    paginator = Paginator(queryset, step)
    if page_num > paginator.num_pages or page_num <= 0:
        page_num = DEFAULT_PAGE
    page = PageAccessor(
        content = paginator.page(page_num).object_list,
        current = page_num,
        last = paginator.num_pages,
        first = DEFAULT_PAGE
    )
    return page

def get_params(request):
    try:
        page = int( request.GET.get("page", str(DEFAULT_PAGE)) )
        return page
    except:
        return DEFAULT_PAGE
    
class QuestionsManager(models.Manager):
    def get_page(self, request, order_by_rating=False, tag=None):
        page_num = get_params(request)
        questions = super().all()
        if tag:
            questions = questions.filter(tags__name=tag)
        if order_by_rating:
            questions = questions.order_by("-rating")
        return get_page(questions, page_num)
    
class AnswersManager(models.Manager):
    def get_page(self, request, question_id):
        page_num = get_params(request)
        answers = super().filter(question__pk=question_id).order_by("-correctness")
        return get_page(answers, page_num)
