import  heapq
li=[1,5,4,7,8,9,2,3]
heapq._heapify_max(li) ##building max heap
print(li)
print(heapq._heappop_max(li))  ##removing max element from max heaap
print(li)
heapq._heapreplace_max(li,0)  ##removing max and replacing it with other element
print(li)
