class Table:
    __store_list = []

    def add_head(self, x):
        self.__store_list.insert(0, x)

    def add_tail(self, x):
        self.__store_list.append(x)

    def del_head(self):
        self.__store_list.pop(0)

    def del_tail(self):
        self.__store_list.pop()

    def is_empty(self):
        return len(self.__store_list) is 0

    def in_table(self, sudoku):
        for record in self.__store_list:
            if record.sudoku.__eq__(sudoku):
                return record
        return None

    def get_table(self):
        return self.__store_list

    def set_table(self, new_list):
        self.__store_list = new_list
