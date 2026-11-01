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
      raise IndexError("heap is empty)
    return self.data[0]
