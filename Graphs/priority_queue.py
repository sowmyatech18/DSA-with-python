class PriorityQueue:
  class Locator:
    def __init__(self,key,value,index):
      self.key=key
      self.value=value
      self.index=index
      
  def __init__(self):
      self.data=[]
  def __len__(self):
    return len(self.data)
  def is_empty(self):
    return len(self.data)==0
  def add(self,key,value):
    loc=self.Locator(key,value,len(self.data))
    self.data.append(loc)
    j=loc.index
    while j>0:           #up heap
      p=(j-1)//2
      if self.data[j].key<self.data[p].key:
        self.data[j],self.data[p]=self.data[p],self.data[j]
        self.data[j].index=j
        self.data[p].index=p
        j=p
      else:
        break
    return loc
  def min(self):
    if self.is_empty():
      raise IndexError("Priority queue has no value")
    return (self.data[0].key,self.data[0].value)
  def remove_min(self):
    if self.is_empty():
      raise IndexError("Priority queue has no value")
    last=len(self.data)-1
    self.data[0],self.data[last]=self.data[last],self.data[0]
    self.data[0].index=0
    loc=self.data.pop()
    j=0
    n=len(self.data)
    while True:
      small=j    #down heap
      left=2*j+1
      right=2*j+2
      if left<n and self.data[left].key<self.data[small].key:
          small=left
      if right<n and self.data[right].key<self.data[small].key:
          small=right
      if small==j:
        break
      self.data[j],self.data[small]=self.data[small],self.data[j]
      self.data[small].index=small
      self.data[j].index=j
      j=small
    return (loc.key,loc.value)
  def update(self,loc,newkey,newvalue):
    loc.key=newkey
    loc.value=newvalue
    j=loc.index

    while j>0:
      p=(j-1)//2
      if self.data[j].key<self.data[p].key:
        self.data[j],self.data[p]=self.data[p],self.data[j]
        self.data[j].index=j
        self.data[p].index=p
        j=p
      else:
        break

    n=len(self.data)
    while True: 
      small=j
      left=2*j+1
      right=2*j+2
      if left<n and self.data[left].key<self.data[small].key:
          small=left
      if right<n and self.data[right].key<self.data[small].key:
          small=right
      if small==j:
        break
      self.data[small],self.data[j]=self.data[j],self.data[small]
      self.data[small].index=small
      self.data[j].index=j
      j=small
      
          
      
    
  
