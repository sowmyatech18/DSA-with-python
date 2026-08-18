def queueArray:
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
