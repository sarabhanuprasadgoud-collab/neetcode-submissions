class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, count = 0, 0
        for i in range(len(nums)):
            count = count + 1 if nums[i] == 1 else 0
            max_count = max(count, max_count)
        return max_count

        