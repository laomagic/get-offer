# def quick_sort(nums):
#     """
#     快排
#     :param nums:
#     :return:
#     """
#     less = []
#     pivotlist = []
#     more = []
#     # 递归出口
#     if len(nums) <= 1:
#         return nums
#     else:
#         # 基准
#         pivot = nums[0]
#         for num in nums:
#             if num < pivot:
#                 less.append(num)
#             elif num > pivot:
#                 more.append(num)
#             else:
#                 pivotlist.append(num)
#         # 对less和more继续进行排序
#         less = quick_sort(less)
#         more = quick_sort(more)
#         return less + pivotlist + more


def quick_sort(nums):
    """
    快排
    :param nums:
    :return:
    """

    # 递归出口
    if len(nums) <= 1:
        return nums
    # 基准
    pivot = nums[0]
    less = [num for num in nums[1:] if num < pivot]  # 取出比基准小的元素
    greater = [num for num in nums[1:] if num >= pivot]  # 取出大于等于基准的元素
    # 对less和more继续进行排序
    less = quick_sort(less)  # 继续排序
    greater = quick_sort(greater)  # 继续排序
    return less + [pivot] + greater


if __name__ == '__main__':
    # nums = [2, 45, 5, 88, 23, 200, 66, 75]
    nums = [200, 88, 75, 2, 45, 66, 23]
    nums_sort = quick_sort(nums)
    print(nums_sort)
