from collections import Counter

def f(n):
    arr=[]
    i=2
    while i<=n:
        if n%i==0:
            arr.append(i)
            n//=i
        else:
            i+=1
    return arr

t=int(input())
for _ in range(t):
    n=int(input())
    arr=f(n)
    C=list(Counter(arr).items())
    for c in C:
        print(*c)