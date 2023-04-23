class PageAccessor:
    def __init__(self, content, current, last, first):
        self.content = content
        self.current = current
        self.last = last
        self.first = first

class PaginationAccessor:
    def __init__(self, page):
        self.needPagination = page.first != page.last
        self.shortPagination = page.first + 1 == page.last
        self.disableNext = page.current == page.last
        self.disablePrev = page.first == page.current
        self.isMoreThanHalf = page.current > (page.last / 2)
        self.next = page.current + 1
        self.prev = page.current - 1
        self.first = page.first
        self.last = page.last
        self.current = page.current