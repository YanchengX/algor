class Node:
    def __init__(self,id, name) -> None:
        self.id = id
        self.name = name
        #structure = node (obj) --node裡專有屬性next
        self.next = None

class Applinklist:
    def __init__(self) -> None:
        self.root = None #Node
        self.tail = None
        
    def isEmpty(self):
        return bool(self.root)

    def insertnode(self, sid, sname):
        nownode = Node(sid, sname)
        if not self.isEmpty():
            self.root = self.tail = nownode
        else:
            self.tail.next = nownode
            self.tail = self.tail.next

    def delnode(self, delid):
        # input del id fine del node
        # tmp = delnode.prev
        # delnode.next = tmp.next
        # delnode remove
        # three situation del in root, in tail, other
        deln = self.root
        while int(delid) != deln.id: deln = deln.next

        if deln.id == self.root.id:
            self.root = self.root.next
        
        elif deln.id == self.tail.id:
            newnode = self.root
            while deln.next.id != self.tail.id: deln = deln.next
            deln.next = self.tail.next
            self.tail = self.tail.next
        
        else:
            newnode = tmp = self.root
            while newnode.id != deln.id:
                tmp = newnode
                newnode = newnode.next
            tmp.next = deln.next

                
    def printlist(self):
        tmp = self.root
        while tmp:
            print('{}:{}'.format(tmp.id, tmp.name))
            tmp = tmp.next
        

if __name__ == "__main__":
    a = ['ys','bs','ca','cad','abc','gg']
    instane = Applinklist()
    for i in range(len(a)): #iterable
        instane.insertnode(i+1,a[i])


    g = input() #i or d
    if g == 'i':
        ip1 = input()
        ip2 = input()
        instane.insertnode(ip1,ip2)
        instane.printlist()
    elif g == 'd':
        ip = input()
        instane.delnode(ip)
        instane.printlist()
    else:
        exit()

