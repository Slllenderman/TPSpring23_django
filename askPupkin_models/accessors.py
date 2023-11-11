class PageAccessor:
    def __init__(self, content, current, last, first):
        self.content = content
        self.current = current
        self.last = last
        self.first = first

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