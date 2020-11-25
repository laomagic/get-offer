# coding:utf-8


def search_index(target, nums):
    """
    二分查找
    :param target: 目标值
    :param nums: 有序数列
    :return: 索引
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return None


if __name__ == '__main__':
    nums = [1, 20, 24, 33, 45, 67, 99]
    target = 99
    index = search_index(target, nums)
    print(index)
