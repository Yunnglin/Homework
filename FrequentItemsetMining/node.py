class Node(object):
    def __init__(self, data, count, parent):
        self.data = data
        self.count = count
        self.parent = parent
        self.child = {}  # {'l1':child1, 'l2': child2}
        self.brother = None

    def count_plus(self, count):
        self.count += count

    def show(self, depth=1):
        print('  ' * depth, self.data, ' ', self.count)
        for child in self.child.values():
            child.show(depth + 1)
