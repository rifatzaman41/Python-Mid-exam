class Hall:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.seats = [[0] * cols for _ in range(rows)]  # 0 represents available seats

    def book_seats(self, show_id, seat_list):
        if show_id == self.get_show_id():
            for row, col in seat_list:
                if 0 <= row < self.rows and 0 <= col < self.cols:
                    if self.seats[row][col] == 0:
                        self.seats[row][col] = 1  # Book the seat
                        print(f"Seat ({row}, {col}) booked successfully.")
                    else:
                        print(f"Seat ({row}, {col}) is already booked.")
                else:
                    print(f"Seat ({row}, {col}) is invalid.")
        else:
            print("Invalid show ID.")

    def get_show_id(self):
                return "12345"



hall = Hall(5, 5)
seat_list = [(0, 0), (1, 1), (2, 2)]
hall.book_seats("12345", seat_list)
