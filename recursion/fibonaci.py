def fibonaaci(n):
    if n==1 or n==2:
        return 1
    return fibonaaci(n-1)+fibonaaci(n-2)
n=int(input())
print(fibonaaci(n))