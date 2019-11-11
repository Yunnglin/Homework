from node import Node


class FPTree(object):
    def __init__(self, dataset, min_support):
        self.null_root = Node('None', 1, None)
        self.header_table = {}
        self.dataset = FPTree.merge_dataset(dataset)
        self.min_support = min_support

    # 合并数据集中的相同项
    @staticmethod
    def merge_dataset(dataset):
        cur_dict = {}
        for items in dataset:
            cur_dict[frozenset(items)] = cur_dict.get(frozenset(items), 0) + 1
        return cur_dict

    # 生成头项表
    def __create_header_table(self):
        table = {}
        for items in self.dataset:
            for item in items:
                table[item] = table.get(item, 0) + self.dataset[items]
        # 筛选满足支持度的项
        table = {k: v for k, v in table.items() if v >= self.min_support}
        # 降序排序
        table = dict(sorted(table.items(), key=lambda item: item[1], reverse=True))
        # 初始化，记录项目重复个数和相邻节点
        for k in table:
            table[k] = [table[k], None]
        return table

    def create_fp_tree(self):
        self.header_table = self.__create_header_table()
        # e.g: {'l2': [7, None], 'l3': [7, None], 'l1': [6, None], 'l5': [2, None], 'l4': [2, None]}
        # print(self.dataset)
        # print(self.header_table)

        freq_item_set = set(self.header_table.keys())
        if len(freq_item_set) == 0:  # 没有频繁项
            return None, None
        # 对项集排序并剔除不符合的项
        for items, count in self.dataset.items():
            cur_dict = {}
            for item in items:
                if item in freq_item_set:
                    cur_dict[item] = self.header_table[item][0]
            if len(cur_dict) > 0:
                ordered_items = [v[0] for v in  # 频度相同时按第二位数字排序
                                 sorted(cur_dict.items(), key=lambda p: (p[1], -ord(p[0][-1])), reverse=True)]
                # print(ordered_items, count)
                self.update_tree(ordered_items, self.null_root, count)
        # self.null_root.show()
        return self.null_root, self.header_table

    def update_tree(self, items, node: Node, count):
        first = items[0]
        if first in node.child:  # 已有
            node.child[first].count_plus(count)
        else:  # 不存在，新建
            new_node = Node(first, count, node)
            node.child[first] = new_node
            # 处理头表
            head: Node = self.header_table[first][1]
            if head is None:  # 头指针中不存在
                self.header_table[first][1] = new_node
            else:  # 存在，向后查找，连接
                while head.brother is not None:
                    head = head.brother
                head.brother = new_node
        # 递归调用，不断构造, 每次向后移动一个元素
        if len(items) > 1:
            self.update_tree(items[1:], node.child[first], count)

    # 生成前缀树
    @staticmethod
    def get_prefix_path(leaf_node: Node):
        path = []
        while leaf_node.parent is not None:
            path.append(leaf_node.data)  # 会添加自身
            leaf_node = leaf_node.parent
        return path

    # 生成条件模式集
    def get_conditional_pattern_bases(self, base):
        tail = self.header_table[base][1]
        cpbs = {}
        while tail is not None:
            prefix_path = FPTree.get_prefix_path(tail)
            if len(prefix_path) > 1:
                cpbs[frozenset(prefix_path[1:])] = tail.count
            tail = tail.brother
        return cpbs

    def mine(self, pre_fix, freq_item_list):
        bases = list(self.header_table.keys())
        bases.reverse()  # 从底向上
        for base in bases:
            new_freq_set = pre_fix.copy()
            new_freq_set.add(base)
            # print('='*50)
            # print('频繁项: ', new_freq_set)
            freq_item_list.append(new_freq_set)
            cpbs = self.get_conditional_pattern_bases(base)
            # print('条件模式基:', base, cpbs)
            new_tree = FPTree(cpbs, self.min_support)
            _tree, _head = new_tree.create_fp_tree()
            if _head is not None:
                # print('条件FP树 ', new_freq_set)
                # _tree.show()
                new_tree.mine(new_freq_set, freq_item_list)


if __name__ == '__main__':
    # data_set = [['l1', 'l2', 'l5'],
    #             ['l2', 'l4','l3'],
    #             ['l2', 'l3','l4'],
    #             ['l1', 'l2','l3', 'l4'],
    #             ['l1', 'l3'],
    #             ['l2', 'l3'],
    #             ['l1', 'l3'],
    #             ['l1', 'l2', 'l3', 'l5'],
    #             ['l1', 'l2', 'l3']]

    stop_word = 'esc'  # 修改终止符
    data_set = []
    print('请输入数据，用逗号分隔每一项，每一行为一项集【输入\'esc\'结束】')
    for line in iter(input, stop_word):
        items = line.replace(" ", "").split(",")
        cur_set = []
        for item in items:
            cur_set.append(item)
        data_set.append(cur_set)
    print(data_set)

    while True:
        try:
            while True:
                min_support = int(input('请输入最小支持度'))
                if 0 <= min_support:
                    print("Min K: " + min_support.__str__())
                    break
                print("请输入正确的支持度")
            break
        except Exception as e:
            print('请输入正确的数字')
    # fp_tree = FPTree(dataset=data_set, min_support=2)
    fp_tree = FPTree(dataset=data_set, min_support=min_support)
    fp_tree.create_fp_tree()
    fre_item_set = []
    fp_tree.mine(set([]), fre_item_set)
    print([x for x in fre_item_set])
