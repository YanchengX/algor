
# list pythonic  pop() -> O(n)
class QueueImplement:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if len(self.queue) < 1:
            print('queue no data')
        else:
            self.queue.pop(0)

    def size(self):
        print(len(self.queue))
    
    def show(self):
#         print(self.queue)

if __name__ == "__main__":

    instanceA = QueueImplement()
    instanceA.enqueue(1)
    instanceA.enqueue(2)
    instanceA.enqueue(3)
    instanceA.enqueue(4)
    instanceA.dequeue()
    instanceA.dequeue()
    
    instanceA.show()

