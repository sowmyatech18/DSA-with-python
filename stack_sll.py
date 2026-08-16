class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stackLinkedList:
    def __init__(self):
        self.head=None
    def push(self,x):
        ni=Node(x)
        if(self.head==None):
            self.head=ni
            return
        ni.next=self.head
        self.head=ni
    def pop(self):
        if(self.head==None):
            print("stack underflow")
            return
        v=self.head.data
        self.head=self.head.next
        return v
    def peek(self):
        if(self.head==None):
            print("empty stack")
            return
        v=self.head.data
        return v

    def display(self):
        if(self.head==None):
            return
        curr=self.head
        while(curr):
            print(curr.data)
            curr=curr.next

s=stackLinkedList()
s.push(4)
s.push(10)
s.push(1)
print(s.pop())
print(s.peek())
print("\n")
s.display()

        
