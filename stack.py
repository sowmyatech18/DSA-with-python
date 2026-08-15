class stackArray:
    def __init__(self,cap):
        self.arr=[0]*cap
        self.cap=cap
        self.top=-1

    def push(self,x):
        if(self.top==(self.cap-1)):
            print("stack overflow")
            return
        self.top+=1
        self.arr[self.top]=x
        

    def pop(self):
        if(self.top==-1):
            print("stack underflow")
            return 
        v=self.arr[self.top]
        self.top-=1
        return v

    def peek(self):
        if(self.top==-1):
            print("empty stack")
        v=self.arr[self.top]
        return v

s=stackArray(4)
s.push(3)
s.push(8)
s.push(1)
s.push(7)
print(s.pop())
print(s.peek())
print(s.arr)

