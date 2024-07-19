class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left , right = 0 , len(nums)-1

        nums = sorted(enumerate(nums) ,key = lambda x:x[1])
        
        while left < right:
            current_sum = nums[left][1] + nums[right][1]
            
            if current_sum == target:
                return [nums[left][0], nums[right][0]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []
      
        