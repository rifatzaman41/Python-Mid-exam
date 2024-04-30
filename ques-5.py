class Show:
    def __init__(self, name, time):
        self.name = name
        self.time = time

class Hall:
    def __init__(self, name):
        self.name = name
        self.shows = []

    def add_show(self, show):
        self.shows.append(show)

    def view_show_list(self):
        if not self.shows:
            print("No shows running currently.")
        else:
            print(f"Shows running in {self.name}:")
            for show in self.shows:
                print(f"{show.name} - Time: {show.time}")

hall = Hall("Main Hall")

show1 = Show("Magic Show", "6:00 PM")
show2 = Show("Comedy Show", "8:00 PM")
show3 = Show("Concert", "10:00 PM")

hall.add_show(show1)
hall.add_show(show2)
hall.add_show(show3)

hall.view_show_list()

