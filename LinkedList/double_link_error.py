class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = LinkedNode(-1)
        self.tail = self.head
                

    def get(self, index: int) -> int:
        i = 0 
        star = self.head
        while i < index:
            if star:
                star = star.next 
                i+=1
            else:
                return -1
        if star:
            return star.next.val
        else:
            return -1
  

    def addAtHead(self, val: int) -> None:
        a = self.head
        self.head.prev = LinkedNode(val)
        self.head = self.head.prev
        self.head.next = a

      

    def addAtTail(self, val: int) -> None:
        b = self.tail
        self.tail.next = LinkedNode(val)
        self.tail =self.tail.next
        self.tail.prev = b
        

    def addAtIndex(self, index: int, val: int) -> None:
            i = 0
            start = self.head
            while i < index and start:
                i+=1
                start = start.next
            if start and start.next:
                a = start.next
                b = a.prev

                start.next = LinkedNode(val)
                start.next.next = a
                start.next.prev = start
                a.prev = start.next
            
            elif start and not start.next:
                b = self.tail
                self.tail.next = LinkedNode(val)
                self.tail =self.tail.next
                self.tail.prev = b

                
                
     

    def deleteAtIndex(self, index: int) -> None:
            i = 0
            start = self.head
            while i < index and start:
                i+=1
                start = start.next
            if start and start.next:
                if start.next.next:
                    #a = start.next


                    start.next = start.next.next
                    start.next.prev = start
                else:
                    start.next = None

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)