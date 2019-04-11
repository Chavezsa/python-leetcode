# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice. 
#
# Example: 
#
# 
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
#
# 
#

# 数组没有明确说明是否有序，认为是无序
# 整数也没有说明一定是正整数，因此不能排序做渐进式的处理
class Solution:
    # 最直观解法,每个元素item判断target - item是否在list，且索引比当前大，是的话 就直接返回
    def twoSum1(self, nums: list, target: int) -> list:
        for location, item in enumerate(nums):
            if (target - item) in nums[location + 1:]:
                return [location, nums.index((target - item), location + 1)]

    def twoSum2(self, nums: list, target: int) -> list:
        length = len(nums)
        for item in range(length):
            for next_item in range(item + 1, length):
                if nums[item] + nums[next_item] == target:
                    return [item, next_item]

    # 讨论区高手用的方法
    def twoSum3(self, nums: list, target: int) -> list:
        wanted_nums = dict()
        for index in range(len(nums)):
            if nums[index] in wanted_nums:
                return [wanted_nums[nums[index]], index]
            else:
                wanted_nums[target - nums[index]] = index

    # 自己用的方法
    def twoSum4(self, nums: list, target: int) -> list:
        wanted_nums = dict()
        for index, item in enumerate(nums):
            if item in wanted_nums:
                return [wanted_nums[item], index]
            else:
                wanted_nums[target - item] = index
