class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    self.prev=None
class circular_dll:
  def __init__(self):
    self.head=None
  def insertathead(self,x):
    ni=Node(x)
    if(self.head==None):
      self.head=ni
      ni.next=self.head
      ni.prev=self.head
      return
    curr=self.head
    while(curr.next!=self.head):
      curr=curr.next
    curr.next=ni
    ni.prev=curr
    ni.next=self.head
    self.head.prev=ni
    self.head=ni
    
      
      
