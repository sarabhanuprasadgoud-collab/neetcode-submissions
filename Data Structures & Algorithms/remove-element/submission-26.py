class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums)
        index = 0
        while (index < last):
            if nums[index] == val:
                nums[index] = nums[last - 1]
                last = last - 1
            else:
                index = index + 1
        return last