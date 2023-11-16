from typing import Any
from django.db import models
from askPupkin_models.pagination import paginate, DEFAULT_PAGE

ORDERS = ("rating", )
    
class QuestionsQueryset(models.QuerySet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    order_by_paramval = ""
    tags = list()

    def get_page(self, request):
        try: page_num = int(request.GET.get("page", DEFAULT_PAGE) )
        except ValueError: page_num = DEFAULT_PAGE
        page = paginate(self, page_num)
        page.path = request.get_full_path()
        return page
    
    def filter_tags(self, request):
        QuestionsQueryset.tags = request.GET.getlist("tag")
        return self.filter(tags__name__in=QuestionsQueryset.tags) if QuestionsQueryset.tags else self
    
    def order_by_param(self, request):
        QuestionsQueryset.order_by_paramval = request.GET.get("order_by", "")
        if QuestionsQueryset.order_by_paramval in ORDERS:
            return self.order_by("-" + QuestionsQueryset.order_by_paramval)
        else:
            QuestionsQueryset.order_by_paramval = ""
            return self
            
        

    
class AnswersManager(models.Manager):
    def get_page(self, request, question_id):
        page_num = request.GET.get("page", DEFAULT_PAGE)
        answers = super().filter(question__pk=question_id).order_by("-correctness")
        return paginate(answers, page_num)
