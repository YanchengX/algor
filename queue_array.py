
# array implement
import numpy as np
class QueueImplement:
    def __init__(self):
        self.Max = 20
        self.queue = np.array([0]*self.Max)
        self.front = self.rear = -1

    def isFull(self):
        return True if self.rear + 1 == self.Max else False

    def isEmpty(self):
        return True if self.rear == -1 else False

    def enqueue(self, val):
        if self.isFull():
            print('queue overflow')
        else:
            if self.rear == -1 and self.front == -1:
                self.rear = self.front = 0
            else:
                self.rear += 1
            self.queue[self.rear] = val

    def dequeue(self):
        if self.isEmpty():
            print('queue no data')
        else:
            self.rear -=1

    def size(self):
        count = 0
        for i in range(self.front, self.rear+1):
            count+=1
        return count

    def show(self):
        for i in range(self.front,self.rear+1):
            print(self.queue[i])

    
if __name__ == "__main__":

    instanceA = QueueImplement()
    instanceA.enqueue(1)
    instanceA.enqueue(2)
    instanceA.enqueue(3)
    instanceA.enqueue(4)
    instanceA.dequeue()
    instanceA.dequeue()
    
    instanceA.show()

