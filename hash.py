#hashtable implement fuction using divide
#and slove overflow and collision using linar probing and double hash(implement by linked-list)

#linar probing

#linar probing有一個缺失就是key值資料相似的會聚在一起
global INDEXBOX
global MAXIMUM
INDEXBOX = 10
MAXIMUM = 7

class Hash:
    def __init__(self):
        self.data = [15,20,10,30,10,10,20]
        self.index = [-1] * INDEXBOX

        for i in range(MAXIMUM):
            self.hashTable(self.data[i], self.index)
        print(self.index)

    def hashTable(self, num, index):
        tmp = num % INDEXBOX

        #實作線性探測法，如果該key位置沒有資料就放置不然就放下一個
        
        while True:
            if index[tmp] == -1:
                index[tmp] = num
                break
            else:
                tmp = (tmp+1) % INDEXBOX

if __name__ == '__main__':
    instane = Hash()
    
