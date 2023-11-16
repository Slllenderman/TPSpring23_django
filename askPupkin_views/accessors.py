from askPupkin_models.models import *

class PaginationAccessor:
    def __init__(self, page):
        self.needPagination = page.first != page.last
        self.shortPagination = page.last == 2 or page.last == 3
        self.disableNext = page.current == page.last
        self.disablePrev = page.first == page.current
        self.isMoreThanHalf = page.current > (page.last / 2)
        self.next = str(page.current + 1)
        self.prev = str(page.current - 1)
        self.first = str(page.first)
        self.last = str(page.last)
        self.current = str(page.current)

class QuestionsAccessors:
    def __init__(self, page, questions):
        self.is_hot = True if questions.order_by_paramval == "rating" else False
        self.tags = questions.tags
        self.questions = page.content
        self.path = page.path
        self.pagination = PaginationAccessor(page)

class AnswersAccessor:
    def __init__(self, request, question_id):
        self.question = Question.objects.get(pk=question_id)
        self.page = Answer.objects.get_page(request, question_id)
        self.answers = self.page.content
        self.pagination = PaginationAccessor(self.page)

    