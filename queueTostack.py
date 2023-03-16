#stack implement using queue
#push pop peek empty

class Stack:

    def __init__(self):
        self.queue = []
        self.main = []
    def isEmpty(self):
        return True if self.queue == None else False

    def push(self, val):
        return 

    def pop(self):
        if self.isEmpty():
            raise Error
        else:
            return self.queue.pop(0)
    def peek(self):
        return

    

if __name__ == "__main":
    instane = Stack()
