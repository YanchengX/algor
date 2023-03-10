class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.next = None
        
class Apllicaitonlist:
    def __init__(self) -> None:
        self.root = None
        self.tail = None
        self.memory = []

    def isEmpty(self):
        return not bool(self.root)

    def insertnode(self,data):
        node = Node(data)

        if self.isEmpty():
            self.root = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
            
        # unique data value (not memory space)
        if node.data not in self.memory:
            self.memory.append(node.data)
        else:
            raise ValueError

    def deletenode(self,value):
        
        if self.root == value:
            self.root = self.root.next
        elif self.tail == value:
            pre = self.root
            while pre.next != self.tail:
                pre = pre.next
            pre.next = self.tail.next
            pre = pre.next
        else:
            pre = self.root
            while pre.next.data != value : pre = pre.next
            delnode = pre.next
            pre.next = delnode.next
            self.tail = pre.next

    def isCycle(self):
        slow = fast = self.root
        
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def reverselist(self):
        #switcher
        # cur = self.root
        # prev = None
        # while cur:
        #     nex = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = nex
        # self.root = prev

        #recursion
        tmp = self.reverse(self.root, prev = None)
        self.root = tmp
    def reverse(self, cur, prev):
        if not cur:
            return prev
        nex = cur.next
        cur.next = prev
        return self.reverse(nex,cur)

    def printlist(self):
        if self.isCycle():
            # #two pointer find prefix cycle On O1
            # slow = fast = self.root
            # while slow.next and fast.next and fast.next.next:
            #     slow = slow.next
            #     fast = fast.next.next
            #     if slow == fast:
            #         break
            # slow = self.root
            # while slow != fast:
            #     slow = slow.next
            #     fast = fast.next
            # print('{} is prefix of cyclelist'.format(slow.data))
            
            
            #find started node using map    TO n*logn SO n
            visit = {}
            node = self.root

            while node.data not in visit:
                visit[node.data] = True
                node = node.next
            print('{} is prefix of cyclelist'.format(node.data))
            

        else:
            tmp = self.root 
            while tmp:
                print('data is {}'.format(tmp.data))
                tmp = tmp.next

if __name__ == "__main__":
    instance = Apllicaitonlist()
    
    data = [1,7,4,8,9,3,6]
    
    #insert
    for val in data:
        instance.insertnode(val)

    #delete
    #instance.deletenode(4)

    #cycle
    #instance.tail.next = instance.root

    #reverse
    instance.reverselist()

    #print
    instance.printlist()