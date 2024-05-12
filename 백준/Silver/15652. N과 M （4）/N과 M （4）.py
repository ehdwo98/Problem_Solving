import sys
sys.setrecursionlimit(10**6)
n,m=map(int,sys.stdin.readline().split())

arr=[]

def nm3(k):
    if k==m:
        print(*arr)
        return
    idx=0
    if k!=0:
        idx=arr[-1]-1
    for i in range(idx,n):
        arr.append(i+1)
        nm3(k+1)
        arr.pop()

nm3(0)