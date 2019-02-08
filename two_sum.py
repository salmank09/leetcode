'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

'''
sol1: 
class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        for index,val in enumerate(nums):
        	for index2, val2 in enumerate(nums):
        		if index != index2 and nums[index] + nums[index2] == target:
        			return [index, index2]
'''

#sol2
class Solution:
	def twoSum(self, nums, target):
		d = {}
		for index, val in enumerate(nums):
			diff = target-val
			if diff in d:
				return [d[diff], index]
			d[val] = index