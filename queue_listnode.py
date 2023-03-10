#implement queue using array, linked-list, list pythonic
#enqueue, dequeue, size, show


# linked-list

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class QueueImplement:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return True if self.front == None else False

    def enqueue(self, val):
        newnode = Node(val)
        if self.isEmpty():
            self.front = self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = self.rear.next

    def dequeue(self):
        if self.isEmpty():
            print('nothing to pop')
        elif self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next

    def show(self):
        tmp = self.front

        while tmp:
            print(tmp.val)
            tmp = tmp.next
    
if __name__ == "__main__":

    instanceA = QueueImplement()
    instanceA.enqueue(1)
    instanceA.enqueue(2)
    instanceA.enqueue(3)
    instanceA.dequeue()
    instanceA.dequeue()
    
    instanceA.show()


