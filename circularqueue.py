class CircularQueue:
    def __init__(self, max_size):
        self.max = max_size  
        self.queue = [0] * self.max  
        self.front = -1  
        self.rear = -1 
    
    def insertion(self, value):

        if (self.rear + 1) % self.max == self.front:
            print("Queue is full, cannot insert element")
        else:
            if self.front == -1:
                self.front = 0
 
            self.rear = (self.rear + 1) % self.max
            self.queue[self.rear] = value
            print(f"Inserted {value} into the queue")
    
    def deletion(self):
        if self.front == -1:
            print("Queue is empty, cannot delete element")
        else:
            print(f"Deleted {self.queue[self.front]} from the queue")
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.max
    
    def traverse(self):
        
        if self.front == -1:
            print("Queue is empty")
            print("Queue elements are:")
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.max
            print()  

ob = CircularQueue(5)  
ob.insertion(10) 
ob.insertion(20)  
ob.insertion(30)  
ob.traverse()  
ob.deletion() 
ob.traverse()  
ob.insertion(40)  
ob.insertion(50)  
ob.insertion(60) 
ob.traverse()  
ob.deletion()  
ob.traverse()  
