class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_index = len(nums) - 1
        index = 0
        while (index <= last_index):
            if nums[index] == val:
                nums[index] = nums[last_index]
                last_index = last_index - 1
            else:
                index = index + 1
        return last_index + 1