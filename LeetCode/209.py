#coding=utf-8

'''
LeetCode 209 长度最小的子数组

解题思路：双指针-滑动窗口
1. 单循环，下标j作为终止位置，并循环
2. 下标i作为起始位置，如滑动的列表和大于等于给定的数字，则起始位置往后移动
3. 返回窗口长度
'''

class Solution:
    def minSubArrayLen(self, nums: list[int], target: int) -> int:
        n = len(nums)
        if (n < 1 or sum(nums) < target): 
            return 0
        i = 0
        x = 0
        res = n + 1  # 最大的窗口不会超过自身长度

        for j in range(0, n):
            x += nums[j]  # 扩大窗口
            while x >= target:
                res = min(res, j-i+1)
                x -= nums[i]  # 缩小窗口
                i += 1
        return res


if __name__ == '__main__':
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    a = Solution()
    print(a.minSubArrayLen(nums, target))