class Stack:
    def __init__(self, size):
        self.l=[]
        self.size=size
        self.top=-1
    def Push(self,element):
        if self.top==self.size-1:
            print("stack is overflow")
        else:
            self.top+=1
            self.l.append(element)
    def Pop(self):
        if self.top==-1:
            print("stack is underflow")
        else:
            self.top-=1
            self.l.pop()
    def Traverse(self):
        for i in range(self.top+1):
            print(self.l[i])

ob=Stack(6)
ob.Push(5)
ob.Traverse()
ob.Push(3)
ob.Push(8)
ob.Push(3)
ob.Pop()
ob.Traverse()