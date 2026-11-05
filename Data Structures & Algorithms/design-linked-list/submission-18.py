class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None


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
            new_node = ListNode(val=val, prev=None, next=self.head)
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.size == 0:
                self.tail = new_node
        elif index == self.size:
            new_node = ListNode(val=val, prev=self.tail, next=None)
            if self.tail:
                self.tail.next = new_node
            self.tail = new_node
        else:
            idx = 0
            curr = self.head
            while idx < index - 1:
                curr = curr.next
                idx = idx + 1
            new_node = ListNode(val, curr, curr.next)
            if curr.next:
                curr.next.prev = new_node
            curr.next = new_node
        self.size = self.size + 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        else:
            curr = self.head
            idx = 0
            while idx < index - 1:
                curr = curr.next
                idx = idx + 1
            node_to_delete = curr.next
            curr.next = node_to_delete.next
            if curr.next:
                curr.next.prev = curr
            else:
                self.tail = curr
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)