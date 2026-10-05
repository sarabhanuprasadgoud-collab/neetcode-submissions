class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] == val:
                nums.pop(idx)
                nums.append('_')
                count = count + 1
        return len(nums) - count