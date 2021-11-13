class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def set_time(self, hours, minutes, seconds):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
        return self.seconds, self.minutes, self.hours


    def get_time(self):
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 00
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 00
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 00

        return Time.get_time(self)



time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())

