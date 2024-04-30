class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity


if __name__ == "__main__":
    hall1 = Hall("Hall 1", 100)
    hall2 = Hall("Hall 2", 150)

    cinema = Star_Cinema()
    cinema.entry_hall(hall1)
    cinema.entry_hall(hall2)

    print(cinema.hall_list)
