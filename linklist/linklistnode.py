class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=Node(3)
b=Node(5)
a.next=b
print(a.data)
print(b.data)
print(a.next.data)
print(a)
print(a.next)
print(b)