# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        while head is not None:
            array.append(head.val)
            head = head.next
        array = array[::-1]
        rev = None
        while array:
            rev = ListNode(array.pop(), rev)
        return rev

        