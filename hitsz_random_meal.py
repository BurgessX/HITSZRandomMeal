"""随机生成要吃什么"""
# 2021/10/26

import random
from typing import List
import openpyxl



def random_stall(stalls:'list[Stall]'):
    """随机显示档口列表中的一个档口"""
    ind = random.randint(0, len(stalls)-1)
    print(f"{stalls[ind].cateen_name}{stalls[ind].floor}楼的{stalls[ind].name}")


class Stall():
    """食堂档口"""
    def __init__(self, name, cateen_name:str, floor:int) -> None:
        self.name = name
        self.cateen_name = cateen_name
        self.floor = floor


class Cateen():
    """食堂"""
    def __init__(self, name, location, stalls:'list[Stall]'=None) -> None:
        """初始化"""
        self.name = name
        self.location = location

        if stalls is not None:
            self.stalls = stalls
            self.stall_num = len(stalls)
            self.stall_names = []
            for stall in stalls:
                self.stall_names.append(stall.name)
        else:
            self.stalls = []
            self.stall_num = 0
            self.stall_names = []

    def show_stalls(self):
        """显示食堂的所有档口"""
        print(f"{self.name}共{self.stall_num}个档口如下：")
        for stall_name in self.stall_names:
            print(f"- {stall_name}")

    def add_stall(self, stall:Stall):
        """新增档口"""
        if stall.cateen_name == self.name:
            self.stalls.append(stall)
            self.stall_num += 1
            self.stall_names.append(stall.name)
        else:
            print(f"新增档口失败！{stall.name}不属于{self.name}。")

    def delete_stall(self, stall_name):
        """删除档口"""
        sum = 0
        for stall in self.stalls:
            if stall.name == stall_name:
                self.stalls.remove(stall)
                self.stall_num -= 1
                self.stall_names.remove(stall_name)
                print(f"成功将{stall_name}从{self.name}中删除。")
                sum += 1

        if sum == 0:
            print(f"删除档口失败！{self.name}中没有{stall_name}。")
        else:
            print(f"共删除了{sum}个档口。")

    def random_stall(self):
        """随机显示食堂的一个档口"""
        ind = random.randint(0, self.stall_num - 1)
        print(self.stall_names[ind])




if __name__ == "__main__":

    """ BUG 各个档口的几率不相同

    # 数据
    # cateens = ['荔园一食堂', '荔园二食堂', '荔园三食堂', '荔园四食堂']
    # cateen1_stalls = ['大众菜', '汤饭和蒸饭', 'U包包', '烤肉拌饭', '妈妈菜（东北菜）',
    #  '西北风味', '二楼自助']
    # cateen2_stalls = ['大众菜', '牛杂', '蒸菜' ,'啫啫煲', '猪脚饭', '小炒', '煲仔饭',
    # '二楼东北菜', '潮汕汤面', '三楼自选']
    # cateen3_stalls = ['大众菜', '饺子', '烧腊', '铁板自选', '麻辣烫', '铁板牛排', '石锅饭']
    # cateen4_stalls = ['两个早餐档口', '大众菜', '麻辣烫', '杭州小笼包',
    # '二楼自选', '锡纸饭', '铁板炒饭', '小炒', '二楼广式烧腊',
    # '肉夹馍', '韩式拌饭', '牛肉饭', '兰州拉面', '西式简餐', '馄饨']

    cateen_choice = random.randint(1, len(cateens))
    print(cateens[cateen_choice-1])
    if cateen_choice == 1:  # 荔园一食堂
        stall_choice = random.randint(0, len(cateen1_stalls)-1)
        print(cateen1_stalls[stall_choice])
    elif cateen_choice == 2:  # 荔园二食堂
        stall_choice = random.randint(0, len(cateen2_stalls)-1)
        print(cateen2_stalls[stall_choice])
    elif cateen_choice == 3:  # 荔园三食堂
        stall_choice = random.randint(0, len(cateen3_stalls)-1)
        print(cateen3_stalls[stall_choice])
    elif cateen_choice == 4:  # 荔园四食堂
        stall_choice = random.randint(0, len(cateen4_stalls)-1)
        print(cateen4_stalls[stall_choice])
    """

    wb = openpyxl.load_workbook('./data.xlsx')
    print(wb.sheetnames)
    stall_ws = wb['档口表']

    # # for row in ws.iter_rows(min_row=2, max_row=3, min_col=1, max_col=2):
    # for row in stall_ws.iter_rows():
    #     for cell in row:
    #         print(cell.value, end='\t')
    #     print()

    # 初始化食堂
    hit_cateens = []
    hit_cateens.extend([
        Cateen('荔园一食堂', '哈工大'),
        Cateen('荔园二食堂', '哈工大'),
        Cateen('荔园三食堂', '哈工大'),
        Cateen('荔园四食堂', '哈工大')
        ])

    # 载入档口数据
    for row in stall_ws.iter_rows(min_row=2):
        stall = Stall(row[0].value, row[1].value, row[2].value)
        if stall.cateen_name == '荔园一食堂':
            hit_cateens[0].add_stall(stall)
        elif stall.cateen_name == '荔园二食堂':
            hit_cateens[1].add_stall(stall)
        elif stall.cateen_name == '荔园三食堂':
            hit_cateens[2].add_stall(stall)
        elif stall.cateen_name == '荔园四食堂':
            hit_cateens[3].add_stall(stall)
        else:
            print('不属于哈工大食堂')
            exit(-1)

    # 打印
    for hit_cateen in hit_cateens:
        hit_cateen.show_stalls()

    # 随机展示档口
    for hit_cateen in hit_cateens:
        hit_cateen.random_stall()

    # 随机展示哈工大食堂中的一个档口
    print("随机展示哈工大食堂中的一个档口：", end='')
    hit_stalls = []
    for hit_cateen in hit_cateens:
        hit_stalls.extend(hit_cateen.stalls)

    random_stall(hit_stalls)
