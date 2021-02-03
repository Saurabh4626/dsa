a="this is string of word it can contain many many word"
k=2
words=a.split() ##list of all words
d={}  

## one way of creating dictionary of frequency of words

# for w in words:
#     if w in d:
#         d[w]+=1
#     else:
#         d[w]=1

## one way of creating dictionary of frequency of words

for w in words:
    d[w]=d.get(w,0)+1
print(d)

for i in d:
    if d[i]==k:
        print(i)
