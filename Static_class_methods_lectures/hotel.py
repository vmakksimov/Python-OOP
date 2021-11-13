


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")


    def add_room(self, room):
        self.rooms.append(room)
        return

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room_number == room.number:
                if not room.is_taken:
                    self.guests += people
                    room.take_room(people)
                    return self.guests


    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                self.guests -= room.guests
                room.free_room()
                return self.guests

    def status(self):
        result = f'Hotel {self.name} has {self.guests} total guests\n'

        free_rooms = []
        taken_rooms = []
        for room in self.rooms:
            if room.is_taken:
                taken_rooms.append(room.number)
            else:
                free_rooms.append(room.number)
        result += f'Free rooms: {", ".join(map(str, free_rooms))}\n'
        result += f'Taken rooms: {", ".join(map(str, taken_rooms))}'

        return result
