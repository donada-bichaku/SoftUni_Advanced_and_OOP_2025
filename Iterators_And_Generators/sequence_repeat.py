class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1

        if self.idx >= self.number:
            raise StopIteration

        return self.sequence[self.idx % len(self.sequence)]




