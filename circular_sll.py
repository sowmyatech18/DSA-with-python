class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def insertathead(self,x):
        ni=Node(x)
        if(self.head==None):
            self.head=ni
            return
        curr=self.head
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
        ni.next=self.head
    def deleteathead(self):
        if(self.head==None):
            return
        if(self.head.next==None):
            self.head=None
            return
        curr=self.head
        self.head=curr.next
        curr=None
    def deleteattail(self):
        if(self.head==None):
            return
        if(self.head.next==None):
            self.head=None
            return
        curr=self.head
        while(curr.next.next):
            curr=curr.next
        curr.next=None
    