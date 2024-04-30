class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []  
        self.rows = rows
        self.cols = cols  
        self.hall_no = hall_no
class Star_Cinema:
    hall_list = []

    def __init__(self):
        pass

    @classmethod
    def add_hall(cls, hall):
        cls.hall_list.append(hall)


hall1 = Hall(rows=10, cols=10, hall_no=1)
Star_Cinema.add_hall(hall1)


