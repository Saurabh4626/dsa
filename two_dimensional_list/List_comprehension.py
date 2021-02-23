list1=[1,2,3,4,5]
list1_1=[2,3,5,7]

##copying into anither list
list2=[i for i in list1]
print(list2)

##copying with condition
list3=[i for i in list1 if i < 3 ]
print(list3)

##copying with multiple condition
list4=[i for i in list1 if i<5 if i>1]
print(list4)

##we can have multiple for loop
## eg intersection of list1 and list1_1
list5=[i for i in list1 for j in list1_1 if i==j]
print(list5)

## using if and else
## eg if in list1 if number is multiple of 2 then
## in new list add square of that number
## else the same number
list6=[i*i if i%2==0 else i for i in list1]
print(list6)

##making list of list
name=['saurabh','tiwari']
list7=[[j for j in i] for i in name]
print(list7)

######   OUTPUTS   #####

# [1, 2, 3, 4, 5]
# [1, 2]
# [2, 3, 4]
# [2, 3, 5]
# [1, 4, 3, 16, 5]
# [['s', 'a', 'u', 'r', 'a', 'b', 'h'], ['t', 'i', 'w', 'a', 'r', 'i']]


