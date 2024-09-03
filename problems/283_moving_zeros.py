from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for n in nums:
            if n == 0:
                nums.remove(n)
                nums.append(0)
        return nums

sol = Solution()

nums = [0,1,0,3,12]
result = sol.moveZeroes(nums)
print(result)
