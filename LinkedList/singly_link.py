class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = LinkedNode(-1)
        self.tail = self.head

    def addnode(self, val):
        self.tail.next = LinkedNode(val)
        self.tail = self.tail.next

    def removenode(self, index):
        start = self.head
        i = 0   
        while i < index and start:
            start = start.next
            i+=1
        if start and start.next:
                if start.next == self.tail:
                        self.tail = start
                
                start.next = start.next.next

    def printnodes(self):
        beg = self.head.next
        while beg != None:
            print(beg.value)
            beg = beg.next
        
            

        
