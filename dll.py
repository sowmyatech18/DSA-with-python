class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None

    def insertathead(self,x):
        ni=Node(x)
        if(self.head==None):
            self.head=ni
            return
        curr=self.head
        curr.prev=ni
        ni.next=curr
        self.head=ni
    def insertattail(self,x):
        ni=Node(x)
        if(self.head==None):
            self.head=ni
            return
        curr=self.head
        while(curr.next):
            curr=curr.next
        curr.next=ni
        ni.prev=curr
        
