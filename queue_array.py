class queueArray:
def __init__(self,cap):
  self.arr=[0]*cap
  self.cap=cap
  self.front=0
  self.rear=-1

  def enqueue(self,x):
    if(self.rear==(self.cap-1)):
      print("queue overflow")
      return
    self.rear+=1
    self.arr[self.rear]=x

  def dequeue(self):
    if(self.front>self.rear):
      print("queue underflow")
      return
    v=self.arr[self.front]
    self.front+=1
    return v

  def peek(self):
    if(self.front>self.rear):
      print("queue empty")
      return
    v=self.arr[self.front]
    return v
    
  def display(self):
    if(self.front>self.rear):
      print("queue empty")
      return
    for i in range(self.front,self.rear+1):
      print(self.arr[i],end=" ")

s=queueArray(4)
s.enqueue(3)
s.enqueue(8)
s.enqueue(10)
s.enqueue(1)
print(s.dequeue())
print(s.peek())
print(s.arr)
s.display()


    
