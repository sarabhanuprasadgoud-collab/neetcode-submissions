class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        occurances = 0
        original_length = length = len(nums)
        index = length - 1
        while (index >= 0):
            if nums[index] == val:
                i = index
                while (i < length - 1):
                    nums[i] = nums[i + 1]
                    i = i + 1
                occurances = occurances + 1
                nums[length - 1] = val
                length = length - 1
            index = index - 1
        k = original_length - occurances
        return k