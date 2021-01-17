def replacechar(s,a,b):
    if len(s)==0:
        return s
    if s[0]==a:
        return b+replacechar(s[1:],a,b)
    return s[0]+replacechar(s[1:],a,b)
print(replacechar("a","a","b"))