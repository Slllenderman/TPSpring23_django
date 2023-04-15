class QuestionsPage_Accessor:
    def __init__(self, questions, active, last, notEnableNext, notEnablePrev):
        self.questions = questions
        self.notEnableNext = notEnableNext
        self.notEnablePrev = notEnablePrev
        if notEnableNext:
            self.prev = active - 3 
            self.active = active - 2
            self.next = active - 1
            self.last = last
        else:
            self.prev = active -1
            self.active = active
            self.next = active + 1
            self.last = last