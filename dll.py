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
    def deleteathead(self):
        #empty list
        if(self.head==None):
            return
        #one element
        if(self.head.next==None):
            self.head=None
            return
        curr=self.head
        self.head=curr.next
        curr.next.prev=None
        curr=None
        
