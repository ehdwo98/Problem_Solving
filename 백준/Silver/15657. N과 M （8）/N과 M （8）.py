import sys
sys.setrecursionlimit(10**6)
n,m=map(int,sys.stdin.readline().split())

arr=list(map(int,sys.stdin.readline().split()))
arr.sort()

isused=[0]*n
arr2=[]

def nm8(k,idx):
    if k==m:
        print(*arr2)
        return
    for i in range(idx,n):
        arr2.append(arr[i])
        nm8(k+1,i)
        arr2.pop()

nm8(0,0)