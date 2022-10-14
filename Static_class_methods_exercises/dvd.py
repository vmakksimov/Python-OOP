mapper = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
          8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False


    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        day, month, year = date.split('.')
        year = int(year)
        month = mapper[int(month)]
        return cls(name, id, year, month, age_restriction)



    def __repr__(self):
        if self.is_rented:
            result = 'rented'
        else:
            result = 'not rented'
        return f'{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {result}'
