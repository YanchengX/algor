#queue implement using stack

class Queue:

    def __init__(self):
        self.temp = []
        self.main = []

    def isEmpty(self):
        return True if len(self.main) == 0 else False
        
    def push(self, val):
        while len(self.main != 0):
            self.temp.append(self.mian.pop())
            
        self.main.append(val)

        while len(self.temp != 0):
            self.main.append(self.temp.pop())

    def pop(self):
        self.main.pop()
        
    def peek(self):
        return self.main[-1]

if __name__ if "__main__":

    instane = Queue()
    