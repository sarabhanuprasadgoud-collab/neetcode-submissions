class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        length = len(nums)
        index = 0
        while (index < length):
            if nums[index] != val:
                nums[pointer] = nums[index]
                pointer = pointer + 1
            else:
                pass # ignore
            index = index + 1
        return pointer