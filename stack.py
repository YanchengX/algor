#stack implement by linked list

#empty, push, pop
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class StackImplement:
    def __init__(self):
        self.top = None
        self.bottom = None

    def isEmpty(self):
        return not bool(self.bottom)
    
    def push(self, val):
        node = Node(val)

        if self.isEmpty():
            self.top = self.bottom = node
        else:
            self.top.next = node
            self.top = node

    def pop(self):
        
        if self.isEmpty():
            print('nothing to pop')
        elif self.bottom == self.top:
            self.bottom = self.top = None
        else:
            tmp = self.bottom
            while tmp.next != self.top:
                tmp = tmp.next
            tmp.next = None
            self.top = tmp

    def peek(self):
        tmp = self.bottom
        
        if not tmp:
            print('nothing in stack')

        while tmp:
            if tmp == self.bottom:
                print('{} -> bottom'.format(tmp.val))
            elif tmp == self.top:
                print('{} -> top'.format(tmp.val))
            else:    
                print(tmp.val)
            tmp = tmp.next

if __name__ == "__main__":
    instaneA = StackImplement()
    
    instaneA.push(3)
    instaneA.push(5)
    instaneA.push(7)
    instaneA.push(9)
    instaneA.push(11)

    instaneA.pop()
    
    instaneA.peek()