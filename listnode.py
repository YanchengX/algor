class Node:
    def __init__(self,id, name) -> None:
        self.id = id
        self.name = name
        self.next = None

class Applinklist:
    def __init__(self) -> None:
        self.root = None #Node
        self.tail = None
        
    def isEmpty(self):
        return bool(self.root)

    def insertnode(self, sid, sname):
        position = sid

        nownode = Node(position, sname)

        if not self.isEmpty():
            self.root = self.tail = nownode
        else:
            self.tail.next = nownode
            self.tail = self.tail.next 

    def delnode(self, delid):
        deln = self.root
        while int(delid) != deln.id: deln = deln.next

        if deln.id == self.root.id:
            self.root = self.root.next
        
        elif deln.id == self.tail.id:
            newnode = self.root
            while newnode.next.id != self.tail.id: newnode = newnode.next
            newnode.next = self.tail.next #現在newnode=5 要把他的next改為tail.next = None
            self.tail = newnode #tail把尾端6刪除擺回newnode現在5的位置
            
        else:
            newnode = self.root
            while newnode.next.id != deln.id:
                newnode = newnode.next
            newnode.next = deln.next

    def printlist(self):
        tmp = self.root
        while tmp:
            print('{}:{}'.format(tmp.id, tmp.name))
            tmp = tmp.next
    
    # #switchs
    # def showreverse(self):
    #     cur = self.root
    #     pre = None

    #     while cur:
    #         nex = cur.next
    #         cur.next = pre
    #         pre = cur
    #         cur = nex
    #     s = ''
    #     while pre:
    #         s += str(pre.id)
    #         pre = pre.next
    #     print(s)

    #recursion
    def showreverse(self):
        rev = self.reverse(self.root, None)
        s = ''
        while rev:
            s += str(rev.id)
            rev = rev.next
        print(s)

    def reverse(self, node, pre):
        if not node:
            return pre
        nex = node.next
        node.next = pre
        return self.reverse(nex, node)


if __name__ == "__main__":

    #data and id
    a = ['ys','bs','ca','cad','abc','gg']
    instane = Applinklist()
    for i in range(len(a)): #iterable
        instane.insertnode(i+1,a[i])

    # g = input() #i or d
    # if g == 'i':
    #     ip1 = int(input())
    #     ip2 = input()
    #     instane.insertnode(ip1,ip2)
    #     instane.printlist()
    # elif g == 'd':
    #     ip = input()
    #     instane.delnode(ip)
    #     instane.printlist()
    # else:
    #     exit()

    instane.showreverse()