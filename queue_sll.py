class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class queueLinkedList:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,x):
        ni=Node(x)
        if(self.rear==None):
            self.front=ni
            self.rear=ni
            return
        self.rear.next=ni
        self.rear=ni
    def dequeue(self):
        if(self.front==None):
            print("queue underflow")
            return
        v=self.front.data
        self.front=self.front.next
        if(self.front==None):
            self.rear=None
        return v
    def peek(self):
        if(self.front==None):
            print("queue underflow")
            return
        v=self.front.data
        return v
    def display(self):
        if(self.front==None):
            print("queue underflow")
            return
        curr=self.front
        while(curr):
            print(curr.data,end=" ")
            curr=curr.next
s=queueLinkedList()
s.enqueue(3)
s.enqueue(8)
s.enqueue(10)
s.enqueue(1)
print(s.dequeue())
print(s.peek())
s.display()
        
        
        
