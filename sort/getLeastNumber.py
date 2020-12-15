class Soulution:
    """
    输入n个整数，找出其中最小的K个数。
    例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。输入n个整数，找出其中最小的K个数。
    例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
    """

    def GetLeastNumbers(self, tinput, k):
        tinput.sort()
        return tinput[:k] if len(tinput) > k else []


if __name__ == '__main__':
    tinput = [4, 2, 10, 5, 30, 80]
    solution = Soulution()
    res = solution.GetLeastNumbers(tinput, 4)
    print(res)

