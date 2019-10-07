class Node:
    children = []
    name = ""
    path = []
    node = {'children': children, 'name': name, 'path': []}

    def __init__(self, children=None, name="", path=None):
        if path is None:
            path = []
        if children is None:
            children = []
        self.children = children
        self.name = name
        self.path = path
        self.node = {'children': children, 'name': name, 'path': path}

    # def set_node(self):
    #     self.node['children'] = self.children
    #     self.node['name'] = self.name
    #     self.node['path'] = self.path

    def add_children(self, node):
        self.children.append(node)

    def find_parent(self, node):
        find_list = self.children
        find_path = node['path'][:-1]
        depth: int = 0
        while True:
            if len(find_path) is 0:
                self.children.append(node)
                return True
            try:
                first = find_list[depth]
            except Exception as e:
                print(e)
                return False
            if first['path'] == find_path:
                first['children'].append(node)
                return True
            # find_list.pop(0)
            depth = depth + 1
            find_list = find_list + first['children']
