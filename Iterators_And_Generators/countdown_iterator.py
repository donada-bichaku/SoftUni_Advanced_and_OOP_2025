class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.idx = self.count + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.idx -= 1

        if self.idx < 0:
            raise StopIteration

        return self.idx


