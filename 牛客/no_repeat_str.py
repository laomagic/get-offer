class Solution:
    """给定一个数组arr，返回arr的最长无的重复子串的长度(无重复指的是所有数字都不相同)。
    方案：对数组遍历， 并使用临时数组保存遍历过的元素， 如果元素出现，则比较并保存当前的最大长度，
    同时临时序列保留相同元素后的无重复序列继续遍历
    """

    def maxLength(self, arr):
        # write code here
        longest_length, cur_seq = 0, []
        for i in arr:
            if i in cur_seq:
                longest_length = max(longest_length, len(cur_seq))
                start = cur_seq.index(i)
                cur_seq = cur_seq[start + 1:]  # 空列表
            cur_seq.append(i)
        return max(longest_length, len(cur_seq))


if __name__ == '__main__':
    arr = [2, 3, 4, 5, 6, 6, 7, 9, 10,11,11]
    solution = Solution()
    length = solution.maxLength(arr)
    print(length)
