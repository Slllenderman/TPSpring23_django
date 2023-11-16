from django.db import models
from .accessors import PageAccessor
from django.core.paginator import Paginator


DEFAULT_PAGE = 1
PAGINATION_STEP = 10
ORDERS = ("rating", )

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
    
class QuestionsManager(models.Manager):
    def get_page(self, request):
        try: page_num = int( request.GET.get("page", DEFAULT_PAGE) )
        except ValueError: page_num = DEFAULT_PAGE
        tags = request.GET.getlist("tag")
        order_by = request.GET.get("order_by", "")
        questions = super().all()

        for tag in tags:
            questions = questions.filter(tags__name=tag)
        
        if order_by in ORDERS:
            questions = questions.order_by("-" + order_by)
        
        return get_page(questions, page_num), tags, True if order_by == "rating" else False

    
class AnswersManager(models.Manager):
    def get_page(self, request, question_id):
        page_num = request.GET.get("page", DEFAULT_PAGE)
        answers = super().filter(question__pk=question_id).order_by("-correctness")
        return get_page(answers, page_num)
