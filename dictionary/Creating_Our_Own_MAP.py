class MapNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class Map:
    def __init__(self):
        self.bucketSize=10
        self.buckets=[None]*self.bucketSize
        self.count=0
    def size(self):
        return self.count

    def getBucketIdex(self,hc):
        return (abs(hc)%self.bucketSize)

    def search_value_from_key(self,key):
        hc=hash(key)
        index=self.getBucketIdex(hc)
        head=self.buckets[index]
        while head is not None:
            if head.key==key:
                return head.value
            head=head.next
        return None
    def remove(self,key):
        self.count -= 1
        hc = hash(key)
        index = self.getBucketIdex(hc)
        head = self.buckets[index]
        prev=None
        while head is not None:
            if head.key==key:
                if prev is None:
                    self.buckets[index]=head.next
                else:
                    prev.next=head.next
                return head.value
            prev=head
            head=head.next

        return None

    def insert(self,key,value):
        hc=hash(key)
        index=self.getBucketIdex(hc)
        head=self.buckets[index]
        while head is not None:
            if head.key==key:
                head.value=value
                return
            head=head.next
        newNode=MapNode(key,value)
        newNode.next=head
        self.buckets[index]=newNode
        self.count+=1
m=Map()
m.insert('saurabh',1)
print(m.size())
m.insert('saurabh',55)
print(m.size())
m.insert('saurabh1',535)
print(m.size())
print(m.search_value_from_key('saurabh1'))
print(m.search_value_from_key('saurabh'))
print(m.remove('saurabh'))
print(m.size())
        
