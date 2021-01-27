class PriorityQueueNode:
    def __init__(self,value,priority):
        self.value=value
        self.priority=priority


class PriorityQueue:
    def __init__(self):
        self.pq=[]
    def getSize(self):
        return len(self.pq)
    def isEmpty(self):
        return self.getSize()==0
    def getMin(self):
        if self.isEmpty() is True:
            return None
        return self.pq[0].value
    def __percolateUP(self):
        childIndex=self.getSize()-1
        while childIndex>0:
            parentIndex=(childIndex-1)//2
            if self.pq[childIndex].priority<self.pq[parentIndex].priority:
                self.pq[childIndex],self.pq[parentIndex]=self.pq[parentIndex],self.pq[childIndex]
                childIndex=parentIndex
            else:
                break
    def insert(self,value,priority):
        pqNode=PriorityQueueNode(value,priority)
        self.pq.append(pqNode)
        self.__percolateUP()

    def __percolateDOWN(self):
        parentIndex=0
        leftChildIndex=2*parentIndex+1
        rightChildIndex = 2 * parentIndex +2
        while leftChildIndex <self.getSize():
            minindex=parentIndex
            if self.pq[minindex].priority >self.pq[leftChildIndex].priority:
                minindex=leftChildIndex
            if rightChildIndex < self.getSize() and self.pq[minindex].priority >self.pq[rightChildIndex].priority:
                minindex=rightChildIndex
            if minindex==parentIndex:
                break
            self.pq[parentIndex],self.pq[minindex]=self.pq[minindex],self.pq[parentIndex]
            parentIndex=minindex
            leftChildIndex = 2 * parentIndex + 1
            rightChildIndex = 2 * parentIndex + 2
    def removeMin(self):
        if self.isEmpty():
            return None
        ele=self.pq[0].value
        self.pq[0]=self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDOWN()
        return ele
pq=PriorityQueue()
pq.insert('A',10)
pq.insert('C',5)
pq.insert('B',19)
pq.insert('D',4)
for i in range(4):
    print(pq.removeMin())
