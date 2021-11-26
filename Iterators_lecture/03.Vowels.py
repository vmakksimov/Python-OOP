


class vowels:


    def __init__(self, text):
        self.text = text
        self.start = 0
        self.vowelss = 'AEIOUYaeiouy'
        self.all_values = [el for el in self.text if el in self.vowelss]
        self.end = len(self.all_values) - 1


    def __iter__(self):
        return self


    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        index = self.start
        self.start += 1
        return self.all_values[index]






my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)