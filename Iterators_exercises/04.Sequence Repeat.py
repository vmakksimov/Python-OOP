class sequence_repeat:
    def __init__(self, text, num):
        self.text = text
        self.num = num
        self.end = num
        self.index = 0
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            if self.index >= len(self.text):
                self.index = 0
            temp = self.text[self.index]
            self.index += 1
            self.start += 1
            return temp
        raise StopIteration




result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
