class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        idx = 0
        curr = self.head
        while idx < index:
            curr = curr.next
            idx = idx + 1
        return curr.val
    

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.head = ListNode(val, self.head)
        else:
            idx = 0
            curr = self.head
            while idx < index - 1:
                curr = curr.next
                idx = idx + 1
            new_node = ListNode(val, curr.next)
            curr.next = new_node
        self.size = self.size + 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            idx = 0
            while idx < index - 1:
                curr = curr.next
                idx = idx + 1
            curr.next = curr.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)