class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        right_max = -1
        index = len(arr) - 1
        while (index >= 0):
            ans[index] = right_max

            i = index
            while (i < len(arr)):
                if arr[i] > right_max:
                    right_max = arr[i]
                i = i + 1

            index = index - 1
        
        return ans
        


        