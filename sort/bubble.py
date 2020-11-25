def bubble_sort(nums):
    """
    冒泡排序：遍历n轮，每轮比较相邻两元素的大小，并且交换位置，
    :param nums: 排序的序列
    :return:
    """
    n = len(nums)
    for i in range(n - 1):
        # 每一轮找出最大的元素
        for j in range(n - i - 1):
            # 比较两个元素的大小
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]  # 交换元素位置
    return nums


if __name__ == '__main__':
    nums = [2, 45, 5, 88, 23, 200, 66, 75]
    nums_sort = bubble_sort(nums)
    print(nums_sort)

