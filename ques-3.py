class Hall:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.show_list = []
        self.seats = {}

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)
        
        
        allocated_seats = [['O' for _ in range(self.cols)] for _ in range(self.rows)]
        
        self.seats[show_id] = allocated_seats

    def display_seats(self, show_id):
        if show_id in self.seats:
            seats = self.seats[show_id]
            for row in seats:
                print(' '.join(row))
        else:
            print("Show ID not found")


hall = Hall(rows=5, cols=10)
hall.entry_show('1', 'Avengers: Endgame', '12:00 PM')


hall.display_seats('1')
