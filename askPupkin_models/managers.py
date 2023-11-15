from typing import Any
from django.db import models
from askPupkin_models.pagination import paginate, DEFAULT_PAGE

ORDERS = ("rating", )
    
class QuestionsManager(models.Manager):
    def get_page(self, request, queryset = None):
        if not queryset:
            queryset = super().all()
        page_num = int(request.GET.get("page", DEFAULT_PAGE) )
        page = paginate(queryset, page_num)
        return page
    
    def filter_tags(self, request, queryset = None):
        if not queryset:
            queryset = super().all()
        tags = request.GET.getlist("tag")
        for tag in tags:
            queryset = queryset.filter(tags__name=tag)
        return queryset, tags
    
    def order_by_params(self, request, queryset = None):
        if not queryset:
            queryset = super().all()
        order_by = request.GET.get("order_by", "")
        if order_by in ORDERS:
            queryset = queryset.order_by("-" + order_by)
        else:
            order_by = ""
        return queryset, order_by
        

    
class AnswersManager(models.Manager):
    def get_page(self, request, question_id):
        page_num = request.GET.get("page", DEFAULT_PAGE)
        answers = super().filter(question__pk=question_id).order_by("-correctness")
        return paginate(answers, page_num)
