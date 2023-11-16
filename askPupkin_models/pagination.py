from django.core.paginator import Paginator

DEFAULT_PAGE = 1
PAGINATION_STEP = 10

class Page:
    def __init__(self, content, current, last, first, path):
        self.content = content
        self.current = current
        self.last = last
        self.first = first
        self.path = path


def paginate(queryset, page_num, step=PAGINATION_STEP):
    paginator = Paginator(queryset, step)
    if page_num > paginator.num_pages or page_num <= 0:
        page_num = DEFAULT_PAGE
    page = Page(
        content = paginator.page(page_num).object_list,
        current = page_num,
        last = paginator.num_pages,
        first = DEFAULT_PAGE,
        path = None
    )
    return page