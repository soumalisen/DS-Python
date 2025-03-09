class LinearQueue:
    def __init__(self, max_size):
        self.max = max_size   
        self.l = [0] * self.max
        self.front = -1
        self.rear = -1  
    
    def insertion(self, value):
        if self.rear == self.max - 1:
            print("Queue is full, element cannot be inserted.")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.l[self.rear] = value
            print(f"Inserted {value} into the queue")
    
    def deletion(self):
        # Check if the queue is empty
        if self.front == -1 :
            print("Queue is empty, cannot delete element")
        else:
            print(f"Deleted {self.l[self.front]} from the queue")
            self.front += 1
    
    def traverse(self):
        if self.front == -1 :
            print("Queue is empty")
        else:
          print("Queue elements are:")
          for i in range(self.front, self.rear + 1):
                print(self.l[i], end=" ")
          print()  


ob = LinearQueue(7)  
ob.insertion(10)  
ob.insertion(20)  
ob.insertion(20)  
ob.traverse()  
ob.deletion()  
ob.traverse()  
ob.insertion(56)  
ob.insertion(10)  
ob.insertion(30)
ob.traverse()  