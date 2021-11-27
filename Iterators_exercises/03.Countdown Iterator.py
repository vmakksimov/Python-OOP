class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.start = self.count
        self.end = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.start >= self.end:
            temp = self.start
            self.start -= 1
            return temp
        raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
