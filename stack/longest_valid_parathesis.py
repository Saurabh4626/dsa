s="(()())"
mc=0
stack=[]
stack.append(-1)
for i in range(len(s)):
    print(stack)
    if s[i]=="(":
        stack.append(i)
    if s[i]==")":
        stack.pop()
        if len(stack)==0:
            stack.append(i)
        else:
            mc=max(mc,i-stack[len(stack)-1])

print(mc)
