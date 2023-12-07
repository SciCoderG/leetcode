from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_dict = {nums[0] : 0}
        for i in range(1,len(nums)):
           missing = target - nums[i]
           try:
               return [value_dict[missing],i]
           except:
               value_dict[nums[i]]=i
        return []
    
sol = Solution()
print(sol.twoSum([3,2,4], 6))
            