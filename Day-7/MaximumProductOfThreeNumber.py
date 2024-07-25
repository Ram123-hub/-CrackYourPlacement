# 628. Maximum Product of Three Numbers
# Easy
# Topics
# Companies
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 6
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:

# Input: nums = [-1,-2,-3]
# Output: -6
 

# Constraints:

# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000

def maximumProduct(nums):
    nums.sort()
    max_product1 = nums[-1] * nums[-2] *nums[-3]
    max_product2 = nums[0]*nums[1]*nums[-1]
    return max(max_product1 , max_product2)


print(maximumProduct([1,2,3]))
print(maximumProduct([1,2,3,4]))
print(maximumProduct([-1,-2,-3]))