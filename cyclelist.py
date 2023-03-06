class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.next = None

class Cyclelist:
    def __init__(self):
        self.root = None
        self.tail = None

    def isEmpty(self):
        return bool(self.root)

    def isCycle(self):
        slow = self.root
        fast = self.root.next

        while fast.next and fast.next.next:
            if slow == fast:
                return 1
            fast = fast.next.next
            slow = slow.next
        return -1

    def insertnode(self, sid, sname):
        node = Node(sid,sname)

        if not self.isEmpty(): 
            self.root = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def printlist(self):
        if not self.isEmpty():
            print("empty list")
        elif self.isCycle() == True:
            count = step = 0
            slow = self.root
            fast = self.root.next
            while count < 2:
                if slow == fast:
                    count +=1
                slow = slow.next
                fast = fast.next.next
                if count == 1:
                    step += 1
            while step>1:
                slow = slow.next
                step -= 1
            print('linklist is cycle and prefix = {}'.format(slow.next.next.id))
        else:
            node = self.root
            while node:
                print('{}:{}'.format(node.id ,node.name))
                node = node.next

if __name__ == "__main__":
    instane = Cyclelist()
    data = ['ys','bs','ca','cad','abc','gg']
    
    for i in range(len(data)):
        instane.insertnode(i,data[i])
    # instane.root = instane.root.next
    instane.tail.next = instane.root
    instane.printlist()
    # print(instane.isCycle())