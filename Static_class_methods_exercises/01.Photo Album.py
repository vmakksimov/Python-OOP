from math import ceil

class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = []
        for num in range(self.pages):
            self.photos.append([])



    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label):
        for row_index in range(len(self.photos)):
            row = self.photos[row_index]
            if len(row) < 4:
                self.photos[row_index].append(label)
                return f'{label} photo added successfully on page {row_index +1} slot {len(self.photos[row_index])}'
        return 'No more free slots'


    def display(self):
        result = ''
        for el in self.photos:
            result += '-'*11 + '\n'
            for index in range(len(el)):
                if index == len(el)-1:
                    result += '[]'
                else:
                    result += '[] '
            result += '\n'
        result += '-'*11 + '\n'
        return result



album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())



