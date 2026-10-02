from typing import List, Set # this adds type hints for List and Set

def list_to_set(nums: List[int]) -> Set[int]:
    seta = set()
    for element in nums:
        seta.add(element)
    return seta


# do not modify below this line
print(list_to_set([1, 2, 3, 4, 5]))
print(list_to_set([1, 1, 2, 2, 3, 3]))
print(list_to_set([1, 2, 3, 4, 5, 5, 5, 3, 4, 5]))
