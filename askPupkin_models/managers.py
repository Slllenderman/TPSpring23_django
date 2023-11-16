from typing import Any
from django.db import models
from askPupkin_models.pagination import paginate, DEFAULT_PAGE

ORDERS = ("rating", )

class QuestionsQueryset(models.QuerySet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.order_by_paramval = ""
        self.tags = list()

    def filter(self, *args, **kwargs):
        filtered = super().filter(*args, **kwargs)
        filtered.order_by_paramval = self.order_by_paramval
        filtered.tags = self.tags
        return filtered

    def order_by(self, *args, **kwargs):
        ordered = super().order_by(*args, **kwargs)
        ordered.tags = self.tags
        ordered.order_by_paramval = self.order_by_paramval
        return ordered

    def get_page(self, request):
        try: page_num = int(request.GET.get("page", DEFAULT_PAGE) )
        except ValueError: page_num = DEFAULT_PAGE
        page = paginate(self, page_num)
        page.path = request.get_full_path()
        return page
    
    def filter_tags(self, request):
        self.tags = request.GET.getlist("tag")
        for tag in self.tags:
            self = self.filter(tags__name=tag)
        return self
    
    def order_by_param(self, request):
        self.order_by_paramval = request.GET.get("order_by", "")
        if self.order_by_paramval in ORDERS:
            return self.order_by("-" + self.order_by_paramval)
        else:
            self.order_by_paramval = ""
            return self
            
        

class AnswersManager(models.Manager):
    def get_page(self, request, question_id):
        try: page_num = int(request.GET.get("page", DEFAULT_PAGE) )
        except ValueError: page_num = DEFAULT_PAGE
        answers = super().filter(question__pk=question_id).order_by("-correctness")
        page = paginate(answers, page_num)
        page.path = request.get_full_path()
        return page
