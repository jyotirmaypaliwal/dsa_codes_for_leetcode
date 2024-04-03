class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left = LinkedNode(0)
        self.right = LinkedNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -=1 
        if curr and curr != self.right and index == 0:
            return curr.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        node, next, prev = LinkedNode(val), self.left.next, self.left
        prev.next = node 
        next.prev = node 
        node.next = next
        node.prev = prev
        

    def addAtTail(self, val: int) -> None:
        node, next, prev = LinkedNode(val), self.right, self.right.prev
        next.prev = node
        prev.next = node 
        node.next = next
        node.prev = prev
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while curr and index > 0:
            curr = curr.next 
            index -=1
        if curr and index == 0:
            node, next, prev = LinkedNode(val), curr , curr.prev
            next.prev = node
            prev.next = node 
            node.next = next
            node.prev = prev
        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while curr and index > 0:
            curr = curr.next 
            index -=1
        if curr and curr != self.right and index == 0:
            next, prev =  curr.next , curr.prev
            next.prev = prev
            prev.next = next

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)