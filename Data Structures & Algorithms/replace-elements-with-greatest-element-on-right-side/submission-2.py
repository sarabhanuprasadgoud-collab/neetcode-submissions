class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        idx = 0
        length = len(arr)
        while (idx < length - 1):
            arr[idx] = max(arr[idx + 1:])
            idx = idx + 1
        arr[length - 1] = -1
        return arr
        