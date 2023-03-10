
#implement queue using array, linked-list, list pythonic
#enqueue, dequeue, size, show

import numpy as np

# array implement
class QueueImplement:
    def __init__(self):
        Max = 20
        self.queue = np.array([0]*Max)
        self.front = self.rear = -1
        
    def enqueue(self, val):
        if self.front   
        self.queue.append(val)

    # def dequeue(self):
    #     if len(self.queue) < 1:
    #         print('queue no data')
    #     else:
    #         self.queue.pop(0)

    # def size(self):
    #     print(len(self.queue))
    
    def show(self):
        print(self.queue)

# # array implement
# class QueueImplement:
#     def __init__(self):
#         self.queue = []
    
#     def enqueue(self, val):
#         self.queue.append(val)

#     def dequeue(self):
#         if len(self.queue) < 1:
#             print('queue no data')
#         else:
#             self.queue.pop(0)

#     def size(self):
#         print(len(self.queue))
    
#     def show(self):
#         print(self.queue)


# # list pythonic  pop() -> O(n)
# class QueueImplement:
#     def __init__(self):
#         self.queue = []
    
#     def enqueue(self, val):
#         self.queue.append(val)

#     def dequeue(self):
#         if len(self.queue) < 1:
#             print('queue no data')
#         else:
#             self.queue.pop(0)

#     def size(self):
#         print(len(self.queue))
    
#     def show(self):
#         print(self.queue)

if __name__ == "__main__":

    instanceA = QueueImplement()
    # instanceA.enqueue(1)
    # instanceA.enqueue(2)
    # instanceA.enqueue(3)
    # instanceA.enqueue(4)
    # instanceA.dequeue()
    # instanceA.dequeue()
    
    instanceA.show()

