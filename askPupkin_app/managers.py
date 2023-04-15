from django.core.paginator import Paginator
from django.db import models
from .accessors import QuestionsPage_Accessor

class QuestionsManager(models.Manager):

    def get_params(self, request):
        page = int( request.GET.get("page", "1") )
        return page

    def get_page(self, request):
        pageNum = self.get_params(request)
        paginator = Paginator(super().all(), 10)
        if (pageNum < 1) or (pageNum > paginator.num_pages):
            pageNum = 1 #ToDo
        page = QuestionsPage_Accessor(
            questions = paginator.page(pageNum).object_list,
            active = pageNum,
            last = paginator.num_pages,
            notEnableNext = pageNum == paginator.num_pages,
            notEnablePrev = pageNum == 1
        )
        return page