"""
栈是一种线性数据结构，用先进后出或者后进先出的方式存储数据，栈中数据的插入删除操作是在栈顶端进行；
常见栈的操作：添加、删除元素 O(1)的复杂度
栈的实现：可以使用列表、链表以及队列
"""

from collections import deque
from queue import LifoQueue


# stack = deque()
# stack.append("世界")
# stack.append("大地")
# stack.append("大爷")
# print(stack)
# res = stack.pop()
# print(res)
# stack = LifoQueue(maxsize=3)
# stack.put("世界")
# stack.put("魔兽")
# stack.put("大千")
# print(stack)
# res = stack.get()
# print(res)

class Stack:
    def __init__(self):
        self.items = []

    def add(self, item):
        """添加元素"""
        self.items.append(item)

    def get(self):
        """获取元素"""
        item = self.items.pop()
        return item

    def __len__(self):
        """栈的长度"""
        return len(self.items)

    def is_empty(self):
        """判断是否为空"""
        return self.items == []


if __name__ == '__main__':
    stack = Stack()
    stack.add("火星")
    stack.add("月球")
    stack.add("地球")
    print(stack.get())
