# 构建大顶堆，从非叶子节点开始倒序遍历，l//2-1是最后一个非叶子节点

class Solution:
    def heap_sort(self, nums):
        i, l = 0, len(nums)
        self.nums = nums
        # 构建大顶堆,从非叶子节点倒序遍历，l//2-1是最后一个非叶子节点
        for i in range(l // 2 - 1, -1, -1):
            self.build_heap(i, l - 1)
        # 根节点和末节点进行交换，重新调整大顶堆
        for j in range(l - 1, -1, -1):
            nums[0], nums[j] = nums[j], nums[0]
            self.build_heap(0, j - 1)
        return nums

    def build_heap(self, i, l):
        """构建大顶堆"""
        nums = self.nums
        left, right = 2 * i + 1, 2 * i + 2
        max_index = i
        if left <= l and nums[i] < nums[left]:
            max_index = left

        if right <= l and nums[left] < nums[right]:
            max_index = right

        if max_index != i:
            nums[i], nums[max_index] = nums[max_index], nums[i]
            self.build_heap(max_index, l)


if __name__ == '__main__':
    nums = [2, 10, 4, 60, 3, 20]
    # s = Solution()
    # nums = s.heap_sort(nums)
    # print(nums)
    l = len(nums)
    for i in range(l - 1, -1, -1):
        print(i)
