import sys
input=sys.stdin.readline

n=int(input())
arr=list(i for i in range(1,n+1))
while arr:
    p=arr.pop(0)
    print(p)
    if arr:
        p=arr.pop(0)
        arr.append(p)
