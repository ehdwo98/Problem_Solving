import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    l,arr=input().split()
    l=int(l)
    arr=list(arr)
    arr.pop(l-1)
    res=''.join(arr)
    print(res)