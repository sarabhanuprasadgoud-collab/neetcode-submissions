class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None] * 2 * n
        for i in range(n):
            ans[i] = ans[ n + i ]= nums[i]
        return ans