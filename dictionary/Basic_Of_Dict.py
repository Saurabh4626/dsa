# a={}
# print(type(a))

# a={
#     "Saurabh":1,
#     "Tiwari":3
# } ##one way of creating dict

# print(a)
# print(len(a))##prints length of dict ====>>>>2

# b=a.copy()
# print(b)

##creating dict from list of set of pairs
# c=dict([("the",3),("temp",6)])
# print(c)
# prints====>>>>{'the': 3, 'temp': 6}

# d=dict.fromkeys(["temp",654,87])
# print(d)
# prints====>>>{'temp': None, 654: None, 87: None}

# d=dict.fromkeys(["temp",654,87],10)
# print(d)
# prints====>>>>>>> {'temp': 10, 654: 10, 87: 10}


# # accesing data from dictionary
# a={1:2,2:5,"list":[1,2,3,4],"dict":{1:6969}}
# print(a[1])  ## 2
# print(a["list"])  ##[1,2,3,4]
# print(a.get(1))   ##2
# print(a.get("dict"))  ##{1: 6969}
# print(a.keys())   ##dict_keys([1, 2, 'list', 'dict'])
# print(a.values())  ##dict_values([2, 5, [1, 2, 3, 4], {1: 6969}])
# print(a.items())  ##  dict_items([(1, 2), (2, 5), ('list', [1, 2, 3, 4]), ('dict', {1: 6969})])

# for i in a:
#     print(i,a[i])
#
# prints ====>1 2
#             2 5
#             list [1, 2, 3, 4]
#             dict {1: 6969}

# for i in a.values():
#     print(i)
# prints====>2
#             5
#             [1, 2, 3, 4]
#             {1: 6969}



### changing dict
# a={1:2,2:5,"list":[1,2,3,4],"dict":{1:6969}}
# a[767]=774
# print(a)  ##{1: 2, 2: 5, 'list': [1, 2, 3, 4], 'dict': {1: 6969}, 767: 774}
# a[1]=78
# print(a)  ##{1: 78, 2: 5, 'list': [1, 2, 3, 4], 'dict': {1: 6969}, 767: 774}


##adding two dict  by using update
##updating a with b
##if two keys are same then we will use value of b
# a={1:2,2:5,"list":[1,2,3,4],"dict":{1:6969}}
# b={1:44,'name':'saurabh'}
# a.update(b)
# print(a)  ##{1: 44, 2: 5, 'list': [1, 2, 3, 4], 'dict': {1: 6969}, 'name': 'saurabh'}

##removing from dict
# a={1:2,2:5,"list":[1,2,3,4],"dict":{1:6969}}
# print(a.pop("list"))  ##[1, 2, 3, 4]
# print(a)  ##{1: 2, 2: 5, 'dict': {1: 6969}}
# del a[1]
# print(a) ##{2: 5, 'dict': {1: 6969}}
# a.clear()
# print(a)  ##{}
# del a
# print(a)  ##NameError: name 'a' is not defined






