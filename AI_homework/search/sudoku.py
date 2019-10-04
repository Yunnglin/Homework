# noinspection SpellCheckingInspection
class Sudoku:
    __sudoku = []
    __directions = ['up', 'right', 'down', 'left']

    def __init__(self, sudoku):
        self.__sudoku = sudoku

    def __move__(self, position, direct):
        t_i = -1
        t_j = -1
        i = position[0]
        j = position[1]
        if direct is 'up':
            t_i = i - 1
            t_j = j
        elif direct is 'right':
            t_i = i
            t_j = j + 1
        elif direct is 'down':
            t_i = i + 1
            t_j = j
        elif direct is 'left':
            t_i = i
            t_j = j - 1
        return t_i, t_j

    # 对于可变对象，python传引用
    def __copy_list__(self, origin_list):
        new_list = []
        for i in range(len(origin_list)):
            new_list.append(list(origin_list[i]))
        return new_list

    def get_sudoku(self):
        return self.__sudoku

    def move(self, position1, direction):
        position2 = self.__move__(position1, direction)
        new_sudoku = self.__copy_list__(self.__sudoku)
        new_sudoku[position2[0]][position2[1]] = self.__sudoku[position1[0]][position1[1]]
        new_sudoku[position1[0]][position1[1]] = self.__sudoku[position2[0]][position2[1]]
        return Sudoku(new_sudoku)

    def posible_move(self, position):
        allow_directions = []
        for direct in self.__directions:
            [t_i, t_j] = self.__move__(position, direct)
            if self.check_position([t_i, t_j]):
                allow_directions.append(direct)
        return allow_directions

    def find_zero(self):
        for i in range(len(self.__sudoku)):
            for j in range(len(self.__sudoku[i])):
                if self.__sudoku[i][j] == 0:
                    return i, j

    def check_position(self, position):
        if 0 <= position[0] < len(self.__sudoku) and 0 <= position[1] < len(self.__sudoku[1]):
            return True
        else:
            return False

    def check_right(self):
        pos = self.__sudoku
        if pos[0][0] is 1 and pos[0][1] is 2 and pos[0][2] is 3 and pos[1][0] is 8 \
                and pos[1][2] is 4 and pos[2][0] is 7 and pos[2][1] is 6 and pos[2][2] is 5:
            return True
        else:
            return False

    __position_dict = {'1': [0, 0], '2': [0, 1], '3': [0, 2], '4': [1, 2],
                       '5': [2, 2], '6': [2, 1], '7': [2, 0], '8': [1, 0]}

    def cal_manhattan(self):
        pos = self.__sudoku
        total = 0
        for i in range(len(pos)):
            for j in range(len(pos[i])):
                if pos[i][j] == 0:
                    continue
                else:
                    total = total + Sudoku.manhattan_distance([i, j], self.__position_dict[str(pos[i][j])])
        return total

    @staticmethod
    def manhattan_distance(x, y):
        return sum(map(lambda i, j: abs(i - j), x, y))

    def __eq__(self, other):
        pos = self.__sudoku
        pos2 = other.get_sudoku()
        for i in range(len(pos)):
            for j in range(len(pos[i])):
                if not pos[i][j] is pos2[i][j]:
                    return False
        return True

    def plot(self):
        pos = self.__sudoku
        print('-------')
        for i in range(len(pos)):
            for j in range(len(pos[i])):
                if j == 0:
                    print('|{0} '.format(pos[i][j]), end='')
                elif j == len(pos[i]) - 1:
                    print(' {0}|'.format(pos[i][j]))
                else:
                    print(pos[i][j], end='')
        print('-------')
