def print1_to_n(n):
    if n==0:
        return
    print(n)
    print1_to_n(n-1)

n=int(input())
print1_to_n(n)