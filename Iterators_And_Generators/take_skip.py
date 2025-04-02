class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.curr = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.curr += 1
        if self.curr == self.count:
            raise StopIteration

        return self.curr * self.step


