class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist():
    def __init__(self):
        self.head= None

    def insertathead(self,x):
        ni=Node(x)
        if self.head==None:
            self.head=ni
            return 
        ni.next=self.head
        self.head=ni

    def insertattail(self,x):
        ni=Node(x)
        #empty list
        if self.head==None:
            self.head=ni
            return
        
        curr=self.head
        while(curr.next):
            curr=curr.next
        curr.next=ni
    
    def deleteathead(self):
        #empty list
        if(self.head==None):
            return
        self.head=self.head.next

    def deleteattail(self):
        #empty list
        if(self.head==None):
            return
        #one element list
        if(self.head.next==None):
            self.head=None
            return
        curr=self.head
        while(curr.next.next):
            curr=curr.next
        curr.next=None

    def displayall(self):
        curr=self.head
        if(curr==None):
            print("empty list")
            return
        while(curr):
            print(curr.data)
            curr=curr.next

    def insertatk(self):
        
l=Linkedlist()
l.insertathead(10)
l.insertattail(2)
l.insertattail(8)
l.insertattail(1)
l.deleteathead()
l.deleteattail()
l.displayall()