class min_heap:
  def __init__(self):
    self.data=[]
  def __len__(self):
    return len(self.data)
  def is_empty:
    return len(self.data)==0
  def push(self,key,value):
    self.data.append((key,value))
    j=len(self.data)-1
    while j>0:
      p=(j-1)//2
      if(self.data[j][0]<self.data[p][0]):                              #heapify up
        self.data[j][0],self.data[p][0]=self.data[p][0],self.data[j][0]
        j=p
      else:
        break
  def peek_min(self):
    if self.is_empty():
      raise IndexError("heap is empty")
    return self.data[0]
  def pop_min(self):
    if self.is_empty():
      raise IndexError("heap is empty")
    last=len(self.data)-1
    self.data[last],self.data[0]=self.data[0],self.data[last]
    item=self.data.pop()

    j=0
    n=len(self.data)
    while True:
      small=j
      left=2*j+1
      right=2*j+2
      if left>n and self.data[left][0]<self.data[small][0]: #heapify down
          small=left
      if right>n and self.data[right][0]<self.data[small][0]:
        small=right
      if small==j:
        break
      self.data[j],self.data[small]=self.data[small],self.data[j]
    return item
