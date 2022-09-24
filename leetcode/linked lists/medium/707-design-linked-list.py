class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1
        if not self.head:
            return -1
        curr_node = self.head
        for i in range(index):
            curr_node = curr_node.next
        return curr_node.val
    

    def addAtHead(self, val: int) -> None:
        newnode = Node(val)
        if not self.head:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        self.length += 1

        
    def addAtTail(self, val: int) -> None:
        newnode = Node(val) 
        if not self.head:
            self.head = newnode
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = newnode
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        newnode = Node(val)
        if index > self.length or index < 0:
            return 
        if index == 0:
            self.addAtHead(val)
        else:
            curr_node = self.head
            for i in range(index-1):
                curr_node = curr_node.next
            newnode.next = curr_node.next
            curr_node.next = newnode
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        curr_node = self.head
        if index >= self.length or index < 0:
            return 
        if index == 0:
            self.head = curr_node.next 
        else:
            for i in range(index-1):
                curr_node = curr_node.next
            unwantednode = curr_node.next
            curr_node.next = unwantednode.next
        self.length -= 1
        
        
        # [1,2,3,4,5]


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)









