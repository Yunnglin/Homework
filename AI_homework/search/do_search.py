from search.NRecord import NRecord
from search.draw_chart import draw_tree
from search.node import Node
from search.sudoku import Sudoku
from search.record import Record
from search.table import Table
from search.tree import Tree

sudoku = [[2, 8, 3],
          [1, 6, 4],
          [7, 0, 5]]
right = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
my_sudo = Sudoku(sudoku)
right_sudo = Sudoku(right)


# print(my_sudo.__eq__(right_sudo))


# res = my_sudo.find_zero()
# print(my_sudo.posible_move(my_sudo.find_zero()))
# new_su = my_sudo.move(my_sudo.find_zero(), 'up')
# print(new_su.get_sudoku())
# new_su.plot()
# print(my_sudo.check_right())

def disp_records(all_record):
    for i in range(len(all_record)):
        print(i)
        for record in all_record[i]:
            print(record.__repr__())


def draw_records(all_record, url):
    data = []
    root = None
    for i in range(len(all_record)):
        for j in range(len(all_record[i])):
            record = all_record[i][j]
            if i == 0 and j == 0:
                root = Node(name=record.sudoku.view(), path=record.path)
                data.append(root.node)
                continue
            cur_node = Node(name=record.sudoku.view(), path=record.path)
            root.find_parent(cur_node.node)
    draw_tree(data, url)


def disp_path(record):
    path = []
    while record:
        path.append(record.sudoku)
        record = record.aim_to
    path.reverse()
    for sudoku in path:
        sudoku.plot()
        print(" -> ")


def breath_first_search(sudoku):
    # 初始化
    table = Table()
    sudo = Sudoku(sudoku)
    record = Record(sudo, 0, [])
    table.add_head(record)
    # TODO
    all_record = [[record]]
    while True:
        if table.is_empty():
            return '搜索结果失败'
        first = table.get_table()[0]
        # 将第一个结点从表中删除
        table.del_head()
        # 深度增加
        new_depth = first.depth + 1
        if first.sudoku.check_right():
            return first.__repr__(), '搜索结果成功'
        directions = first.sudoku.posible_move(first.sudoku.find_zero())
        # TODO
        temp_record = []
        for direction in directions:
            new_sudoku = first.sudoku.move(first.sudoku.find_zero(), direction)
            # 不能直接使用append 可直接list相加
            new_path = first.path + [direction]
            new_record = Record(new_sudoku, new_depth, new_path)
            # TODO
            temp_record.append(new_record)
            if new_sudoku.check_right():
                # TODO
                all_record.append(temp_record)
                draw_records(all_record, 'breath_first_search.html')
                disp_records(all_record)
                return new_record.__repr__(), '搜索结果成功'
            else:
                table.add_tail(new_record)
        # TODO
        all_record.append(temp_record)


def depth_first_search(sudoku):
    # 初始化
    table = Table()
    sudo = Sudoku(sudoku)
    record = Record(sudo, 0, [])
    table.add_head(record)
    # TODO
    all_record = [[record]]
    while True:

        if len(table.get_table()) > 100:
            draw_records(all_record, 'depth_first_search.html')
            disp_records(all_record)
            break
        if table.is_empty():
            return '搜索结果失败'
        first = table.get_table()[0]
        # 将第一个结点从表中删除
        table.del_head()
        # 深度增加
        new_depth = first.depth + 1
        if first.sudoku.check_right():
            return first.__repr__(), '搜索结果成功'
        directions = first.sudoku.posible_move(first.sudoku.find_zero())
        # TODO
        temp_record = []
        for direction in directions:
            new_sudoku = first.sudoku.move(first.sudoku.find_zero(), direction)
            # 不能直接使用append 可直接list相加
            new_path = first.path + [direction]
            new_record = Record(new_sudoku, new_depth, new_path)
            # TODO
            temp_record.append(new_record)
            if new_sudoku.check_right():
                # TODO
                all_record.append(temp_record)
                disp_records(all_record)
                return new_record.__repr__(), '搜索结果成功'
            else:
                table.add_head(new_record)
        # TODO
        all_record.append(temp_record)


def branch_and_bound(sudoku):
    # 初始化
    table = Table()
    sudo = Sudoku(sudoku)
    record = Record(sudo, 0, [])
    table.add_head(record)
    # 定义最大深度为100
    d_max = 5
    # TODO
    all_record = [[record]]
    while True:
        if table.is_empty():
            return '搜索结果失败'
        first = table.get_table()[0]
        # 将第一个结点从表中删除
        table.del_head()
        # 深度增加
        new_depth = first.depth + 1
        if new_depth > d_max:
            continue
        if first.sudoku.check_right():
            return first.__repr__(), '搜索结果成功'
        directions = first.sudoku.posible_move(first.sudoku.find_zero())
        # TODO
        temp_record = []
        for direction in directions:
            new_sudoku = first.sudoku.move(first.sudoku.find_zero(), direction)
            # 不能直接使用append 可直接list相加
            new_path = first.path + [direction]
            new_record = Record(new_sudoku, new_depth, new_path)
            # TODO
            temp_record.append(new_record)
            if new_sudoku.check_right():
                # TODO
                all_record.append(temp_record)
                draw_records(all_record, 'branch_and_bound.html')
                disp_records(all_record)
                return new_record.__repr__(), '搜索结果成功'
            else:
                table.add_tail(new_record)
        # TODO
        all_record.append(temp_record)


def mountain_climbing(sudoku):
    # 初始化
    table = Table()
    sudo = Sudoku(sudoku)
    record = NRecord(sudo, 0, [], sudo.cal_manhattan())
    best_fn = sudo.cal_manhattan()
    table.add_head(record)

    # TODO
    all_record = [[record]]
    while True:
        if table.is_empty():
            return '搜索结果失败'
        first = table.get_table()[0]
        # 将第一个结点从表中删除
        table.del_head()
        # 深度增加
        new_depth = first.depth + 1
        if first.sudoku.check_right():
            return first.__repr__(), '搜索结果成功'
        directions = first.sudoku.posible_move(first.sudoku.find_zero())
        # TODO
        temp_record = []
        for direction in directions:
            new_sudoku = first.sudoku.move(first.sudoku.find_zero(), direction)
            # 不能直接使用append 可直接list相加
            new_path = first.path + [direction]
            new_manhattan = new_sudoku.cal_manhattan()
            new_record = NRecord(new_sudoku, new_depth, new_path, new_manhattan)
            # TODO
            if new_manhattan < best_fn:
                best_fn = new_manhattan
                temp_record.clear()
                temp_record.append(new_record)
            if new_sudoku.check_right():
                # TODO
                all_record.append(temp_record)
                draw_records(all_record, 'mountain_climbing.html')
                disp_records(all_record)
                return new_record.__repr__(), '搜索结果成功'
            else:
                table.add_tail(new_record)
        # TODO
        all_record.append(temp_record)


def best_first_search(sudoku):
    # 初始化
    table = Table()
    sudo = Sudoku(sudoku)
    record = NRecord(sudo, 0, [], sudo.cal_manhattan())
    table.add_head(record)

    # TODO
    all_record = [[record]]
    while True:
        if table.is_empty():
            return '搜索结果失败'
        first = table.get_table()[0]
        # 深度增加
        new_depth = first.depth + 1
        if first.sudoku.check_right():
            return first.__repr__(), '搜索结果成功'
        directions = first.sudoku.posible_move(first.sudoku.find_zero())
        # TODO
        temp_record = []
        for direction in directions:
            new_sudoku = first.sudoku.move(first.sudoku.find_zero(), direction)
            # 不能直接使用append 可直接list相加
            new_path = first.path + [direction]
            new_manhattan = new_sudoku.cal_manhattan()
            new_record = NRecord(new_sudoku, new_depth, new_path, new_manhattan)
            # TODO
            temp_record.append(new_record)
            if new_sudoku.check_right():
                # TODO
                all_record.append(temp_record)
                draw_records(all_record, 'best_first_search.html')
                disp_records(all_record)
                return new_record.__repr__(), '搜索结果成功'
            else:
                table.add_tail(new_record)
        # TODO
        table.set_table(sorted(table.get_table(), key=lambda mrecord: mrecord.f_n))
        all_record.append(temp_record)


def a_star(sudoku):
    # 初始化open和closed表
    open_table = Table()
    closed_table = Table()

    sudo = Sudoku(sudoku)
    first_record = NRecord(sudo, 0, [], sudo.cal_manhattan(), None)
    open_table.add_head(first_record)
    # 初始化tree结构
    tree = Tree()
    tree.add(first_record)

    # TODO
    all_record = [[first_record]]
    while True:
        if open_table.is_empty():
            return '搜索结果失败'
        first = open_table.get_table()[0]
        # node = tree.find_node(first.sudoku)
        open_table.del_head()
        closed_table.add_tail(first)

        # 深度增加
        new_depth = first.depth + 1
        if first.sudoku.check_right():
            return first.__repr__(), '搜索结果成功'
        directions = first.sudoku.posible_move(first.sudoku.find_zero())
        # TODO
        temp_record = []
        for direction in directions:
            new_sudoku = first.sudoku.move(first.sudoku.find_zero(), direction)
            # 不能直接使用append 可直接list相加
            new_path = first.path + [direction]
            new_fn = new_sudoku.cal_manhattan() + new_depth
            new_record = NRecord(new_sudoku, new_depth, new_path, new_fn, first)
            # TODO
            temp_record.append(new_record)

            # 属于open
            open_record = open_table.in_table(new_sudoku)
            closed_record = closed_table.in_table(new_sudoku)
            if open_record:
                if open_record.depth > new_record.depth:
                    open_record.set(new_record)
            # 属于closed表
            elif closed_record:
                if closed_record.depth > new_record.depth:
                    closed_record.set(new_record)
                    _directions = closed_record.sudoku.posible_move(closed_record.sudoku.find_zero())
                    for _direction in _directions:
                        new_sudoku = closed_record.sudoku.move(closed_record.sudoku.find_zero(), _direction)
                        open_record = open_table.in_table(new_sudoku)
                        closed_record = closed_table.in_table(new_sudoku)
                        if open_record:
                            if open_record.depth > new_record.depth:
                                open_record.set(new_record)
                            elif closed_record:
                                if closed_record.depth > new_record.depth:
                                    closed_record.set(new_record)

            # 不属于open，也不属于closed
            else:
                open_table.add_tail(new_record)
                tree.add(new_record)

            if new_sudoku.check_right():
                # TODO
                all_record.append(temp_record)

                disp_records(all_record)
                draw_records(all_record, 'A_star.html')
                disp_path(new_record)
                return new_record.__repr__(), '搜索结果成功'
        # TODO
        open_table.set_table(sorted(open_table.get_table(), key=lambda mrecord: mrecord.f_n))
        all_record.append(temp_record)


# print(breath_first_search(sudoku))
# print(depth_first_search(sudoku))
# print(branch_and_bound(sudoku))
# print(mountain_climbing(sudoku))
# print(best_first_search(sudoku))
print(a_star(sudoku))
