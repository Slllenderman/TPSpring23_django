from django.core.paginator import Paginator

DEFAULT_PAGE = 1
PAGINATION_STEP = 2

class Page:
    def __init__(self, content, current, last, first):
        self.content = content
        self.current = current
        self.last = last
        self.first = first
        self.path = None
        self.user = None


def paginate(queryset, page_num = 0, end = False, step=PAGINATION_STEP):
    paginator = Paginator(queryset, step)
    if page_num > paginator.num_pages or page_num <= 0:
        page_num = DEFAULT_PAGE
    if end:
        page_num = paginator.num_pages
    page = Page(
        content = paginator.page(page_num).object_list,
        current = page_num,
        last = paginator.num_pages,
        first = DEFAULT_PAGE
    )
    return page