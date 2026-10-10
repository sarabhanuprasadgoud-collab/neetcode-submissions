class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None] * 2 * n
        for i in range(len(ans)):
            ans[i] = nums[i % n]
        return ans