class Tree:
    __tree = []

    def add(self, x):
        self.__tree.append(x)

    def find_node(self, sudoku):
        for node in self.__tree:
            if node.sudoku.__eq__(sudoku):
                return node
