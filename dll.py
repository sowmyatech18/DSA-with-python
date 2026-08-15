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
            return
        while(curr):
            print(curr.data)
            curr=curr.next
    def insertatk(self,k,x):
        ni=Node(x);
        curr=self.head
        count=0
        while(curr):
            count+=1
            curr=curr.next
        if(k==0):
            self.insertathead(x)
        if(k==(count-1)):
            self.insertattail(x)
        if(k<0 or k>count):
            print("Out of range")
        curr=self.head
        for i in range(k):
            curr=curr.next
        ni.prev=curr.prev
        curr.prev.next=ni
        ni.next=curr
        curr.prev=ni
    def insertatkback(self,k,x):
            ni=Node(x);
            curr=self.head
            count=0
            while(curr):
                count+=1
                curr=curr.next
            if(k==0):
                self.insertathead(self,x)
            if(k==(count-1)):
                self.insertattail(self,x)
            if(k<0 or k>count):
                print("Out of range")
            curr=self.head
            for i in range(count-k-1):
                curr=curr.next
            ni.prev=curr
            ni.next=curr.next
            curr.next=ni
            ni.next.prev=ni
        
