"""
# Python 3.7
# Ref: http://www.cnblogs.com/llhthinker/p/6719779.html
# Date: 2019-10-21
"""
from datetime import datetime

data_set = [['l1', 'l2', 'l5'],
            ['l2', 'l4'],
            ['l2', 'l3'],
            ['l1', 'l2', 'l4'],
            ['l1', 'l3'],
            ['l2', 'l3'],
            ['l1', 'l3'],
            ['l1', 'l2', 'l3', 'l5'],
            ['l1', 'l2', 'l3']]


# noinspection SpellCheckingInspection,PyPep8Naming
class Apriori(object):
    def __init__(self, dataset, min_confidence, min_support, max_k):
        self.dataset = dataset
        self.max_k = max_k
        self.min_support = min_support
        self.min_confidence = min_confidence
        self.support_data = {}
        self.freq_itemsets = []
        self.C1 = set()

    # 创建C1项集
    def create_C1(self):
        for _set in self.dataset:
            for item in _set:
                # 变成不可变集合
                self.C1.add(frozenset([item]))
        return self.C1

    # 判断项集是否剪枝
    @staticmethod
    def whether_cut(Ck_items, Lksub1_set):
        for item in Ck_items:
            sub_items = Ck_items - frozenset([item])
            if sub_items not in Lksub1_set:
                return False
        return True

    # L(k-1)集自身连接，生成Ck集合
    @staticmethod
    def create_Ck(Lksub1_set, k):
        Ck = set()
        len_Lksub1 = len(Lksub1_set)
        list_Lksub1 = list(Lksub1_set)
        for i in range(len_Lksub1):
            for j in range(1, len_Lksub1):
                same = [x for x in list_Lksub1[i] if x in list_Lksub1[j]]  # 两个列表表都存在
                if len(same) == k - 2:
                    Ck_item = list_Lksub1[i] | list_Lksub1[j]  # 两个列表并集
                    if Apriori.whether_cut(Ck_item, Lksub1_set):
                        Ck.add(Ck_item)
        return Ck

    # 从Ck集合创建Lk集合
    def create_Lk(self, Ck):
        Lk = set()
        frequency_dict = {}
        for item in Ck:
            for _set in self.dataset:
                if item.issubset(_set):  # 在原始数据中找到
                    if item not in frequency_dict:
                        frequency_dict[item] = 1
                    else:
                        frequency_dict[item] += 1
        for item in frequency_dict:
            cur_support: float = frequency_dict[item] / float(len(data_set))
            # 是否满足最小支持度
            if cur_support >= self.min_support:
                Lk.add(item)
                self.support_data[item] = cur_support
        return Lk

    # 开始挖掘
    def mining(self):
        self.create_C1()
        L1 = self.create_Lk(self.C1)
        L_set = []
        Lksub1_set = set(L1)
        L_set.append(Lksub1_set)
        for k in range(2, self.max_k + 1):
            Ck = self.create_Ck(Lksub1_set, k)
            Lk = self.create_Lk(Ck)
            Lksub1_set = set(Lk)
            L_set.append(Lksub1_set)
        return L_set

    # 产生强关联规则
    def create_strong_association(self, L_set):
        strong_associations = []
        sub_sets = []
        for k in range(len(L_set)):
            for freq_set in L_set[k]:
                for sub_set in sub_sets:
                    if sub_set.issubset(freq_set):
                        confidence = self.support_data[freq_set] / self.support_data[sub_set]
                        cur_association = ( sub_set, freq_set-sub_set, confidence)
                        if confidence >= self.min_confidence and cur_association not in strong_associations:
                            strong_associations.append(cur_association)
                sub_sets.append(freq_set)
        return strong_associations


if __name__ == '__main__':
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
                max_k = int(input('请输入最大项集数目: '))
                if 2 <= max_k:
                    print("Max K: " + max_k.__str__())
                    break
                print("请输入正确的项集数目")
            while True:
                min_support = float(input('请输入最小支持度[0, 1]: '))
                if 0 <= min_support <= 1:
                    print("Min support: " + min_support.__str__())
                    break
                print("请输入正确的支持度大小")
            while True:
                min_confidence = float(input('请输入最小置信度[0, 1]: '))

                if 0 <= min_confidence <= 1:
                    print("Min confidence: " + min_confidence.__str__())
                    break
                print("请输入正确的置信度大小")
            break
        except Exception as e:
            print('请输入正确的数字')

    apriori = Apriori(data_set, min_support=min_support, min_confidence=min_confidence, max_k=max_k)
    L_set = apriori.mining()
    association = apriori.create_strong_association(L_set)
    for Lk in L_set:
        if len(Lk) == 0:
            break
        print('L' + len(list(Lk)[0]).__str__() + '项集')
        print('-' * 30)
        for freq_set in Lk:
            print(list(freq_set).__str__(), "\t 支持度 = %.2f" % apriori.support_data[freq_set])
        print('-' * 30)

    print("强关联规则")
    print('=' * 50)
    for s in association:
        print(list(s[0]).__str__(), " => ", list(s[1]).__str__(), "\t 置信度 = %.2f" % s[2])
