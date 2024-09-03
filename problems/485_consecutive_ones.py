
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        result = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                result = max(count, result)
                count = 0
        return max(result, count)
