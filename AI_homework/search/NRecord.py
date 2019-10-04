from search.record import Record


class NRecord(Record):
    f_n = None
    aim_to = None

    def __init__(self, sudoku, depth, path, f_n, aim_to=None):
        super().__init__(sudoku, depth, path)
        self.f_n = f_n
        self.aim_to = aim_to

    def set(self, record):
        self.aim_to = record.aim_to
        self.f_n = record.f_n
        self.path = record.path
        self.depth = record.depth
        self.sudoku = record.sudoku

    def __repr__(self):
        if self.aim_to:
            return {'f(n)': self.f_n, 'sudoku': self.sudoku.get_sudoku(), 'aim_to': self.aim_to.sudoku.get_sudoku()}
        else:
            return {'depth': self.depth, 'f(n)': self.f_n, 'path': self.path, 'sudoku': self.sudoku.get_sudoku()}
