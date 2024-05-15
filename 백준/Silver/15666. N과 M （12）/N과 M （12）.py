import sys
sys.setrecursionlimit(10**6)
n,m=map(int,sys.stdin.readline().split())

arr=list(map(int,sys.stdin.readline().split()))
arr.sort()

arr2=[]

def nm12(idx):
    if len(arr2)==m:
        print(*arr2)
        return
    remember=0
    for i in range(idx,n):
        if remember!=arr[i]:
            arr2.append(arr[i])
            remember=arr[i]
            nm12(i)
            arr2.pop()

nm12(0)