class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        rotations = 0
        while students and rotations < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                rotations = 0
            else:
                removed = students.pop(0)
                students.append(removed)
                rotations = rotations + 1

        return len(sandwiches)