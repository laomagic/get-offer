"""
队列具有先进先出的特点，可以使用列表或者链表实现
双端队列：是一种具有队列和栈的性质的数据结构，双端队列中的元素
可以从两端弹出，其限定插入和删除操作在表的两端进行。
双端队列可以再队列任意端入队和出队
"""


class Quene:
    """列表"""

    def __init__(self):
        self.items = []

    def is_empyty(self):
        return self.items == []

    def add(self, item):
        """添加元素"""
        self.items.append(item)

    def get(self):
        """获取元素"""
        item = self.items.pop(0)
        return item

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    q = Quene()
    q.add("世界")
    q.add("魔兽")
    q.add("大千")
    print(q.get())
    print(q.get())
    print(q.get())
