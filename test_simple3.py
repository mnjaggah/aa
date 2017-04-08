from test_simple4 import text_format
class Dojo(object):
    def __init__(self):
        self.total_rooms = []
        self.offices = []
        self.living_spaces = []
        self.unoccupied_offices = []
        self.unoccupied_living_spaces = []
        self.occupied_offices = []
        self.occupied_living_spaces = []
        self.total_people = []
        self.staff = []
        self.fellows = []

    def create_room(self, room_type, room_name):
        print(self.total_rooms)
        if [office for office in room_name if office in self.total_rooms]:
            print('sorry that room name already exists')
        else:
            if room_type == "office":
                for rm in room_name:
                    self.offices.append(rm)
                    self.unoccupied_offices.append(rm)
                    self.total_rooms.append(rm)
                    print(text_format.CBOLD + 'An office called {0} has been successfully created!'.format(rm) + text_format.CEND)
                    print(self.total_rooms)
            elif room_type == "living":
                for rm in room_name:
                    self.living_spaces.append(rm)
                    self.unoccupied_living_spaces.append(rm)
                    self.total_rooms.append(rm)
                    print('A living space called {0} has been successfully created!'.format(rm))
                    print(self.total_rooms)
dojo = Dojo()
dojo.create_room("office", "maria")