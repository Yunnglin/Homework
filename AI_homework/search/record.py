# noinspection SpellCheckingInspection
class Record:
    depth = 0
    path = []
    sudoku = None

    def __init__(self, sudoku, depth, path):
        self.sudoku = sudoku
        self.depth = depth
        self.path = path

    def to_dict(self):
        return {'depth': self.depth, 'path': self.path, 'sudoku': self.sudoku.get_sudoku()}
