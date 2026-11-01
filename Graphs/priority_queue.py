class PriorityQueue:
  class Locator:
    def __init__(self):
      self.data=[]
    def __len__(self):
      return len(self.data)
    def is_empty(self):
      return len(self.data)==0
    def add(self,key,value):
      loc=Locator(key,value,len(self.data))
      self.data.append(loc)
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
      return loc
    def min(self):
      if self.is_empty():
        raise IndexError("PQ has no value")
      return (self.data[0].key,self.data[0].value)
    
  
