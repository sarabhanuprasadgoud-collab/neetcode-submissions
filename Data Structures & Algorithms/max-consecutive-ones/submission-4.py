class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        idx = 0
        count = 0
        max_count = 0
        length = len(nums)
        while (idx < length):
            if nums[idx] == 1:
                count = count + 1
            else:
                count = 0
            if count > max_count:
                max_count = count
            idx = idx + 1
        return max_count

        