class node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def insertnode(self,data):
        pass
    def delnode(self, data):
        pass
    def nownode(self):
        print(self.data)

class app:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
    
    def info(self):
        print("{}:{}".format(self.id, self.name))


if __name__ == "__main__":
    a = ['ys','bs','ca','cad','abc','gg']
    f = []
    for i,data in enumerate(a):
        ff = app(i,data)
        ff.info()
    