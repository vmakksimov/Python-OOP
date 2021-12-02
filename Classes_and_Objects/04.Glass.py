class Glass:
    """ this class is responsible for checking the free space of a glass"""
    capacity = 250

    def __init__(self):
        self.content = 0


    def fill(self, ml):
        if not ml > (Glass.capacity - self.content):
            self.content += ml
            return f'Glass filled with {ml} ml'
        return f'Cannot add {ml} ml'

    def empty(self):
        self.content = 0
        return 'Glass is now empty'

    def info(self):
        return f"{Glass.capacity - self.content} ml left"


glass = Glass()

