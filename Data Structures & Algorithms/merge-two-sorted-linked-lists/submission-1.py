# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        array1, array2 = [], []
        while list1:
            array1.append(list1.val)
            list1 = list1.next
        while list2:
            array2.append(list2.val)
            list2 = list2.next
        comb_array = array1 + array2
        comb_array.sort()
        comb_list = None
        while comb_array:
            comb_list = ListNode(comb_array.pop(), comb_list)
        return comb_list
            




            
