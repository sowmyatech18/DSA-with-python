class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class circular_sll:
    def __init__(self):
        self.head=None
        
    def insertathead(self,x):
        ni=Node(x)
        if(self.head==None):
            self.head=ni
            ni.next=self.head
            return
        curr=self.head
        ni.next=curr
        self.head=ni
        while(curr.next!=self.head):
            curr=curr.next
        curr.next=self.head
        
    def insertattail(self,x):
        ni=Node(x)
        if(self.head==None):
            self.head=ni
            ni.next=self.head
            return
        curr=self.head
        while(curr.next!=self.head):
            curr=curr.next
        curr.next=ni
        ni.next=self.head
    def deleteathead(self):
        if(self.head==None):
            return
        if(self.head.next==self.head):
            self.head=None
            return
        curr=self.head
        while(curr.next!=self.head):
            curr=curr.next
        self.head=self.head.next
        curr.next=self.head
    def deleteattail(self):
        if(self.head==None):
            return
        if(self.head.next==self.head):
            self.head=None
            return
        curr=self.head
        while(curr.next.next!=self.head):
            curr=curr.next
        curr.next=self.head

    
