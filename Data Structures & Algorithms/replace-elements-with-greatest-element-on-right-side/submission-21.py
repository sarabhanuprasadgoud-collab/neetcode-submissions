class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        index = len(arr) - 1
        right_max = -1
        while (index >= 0):
            original = arr[index]
            arr[index] = right_max
            if original > right_max: 
                right_max = original
            index = index - 1
        return arr
        


        