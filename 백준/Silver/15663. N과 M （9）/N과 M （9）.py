import sys
sys.setrecursionlimit(10**6)
n,m=map(int,sys.stdin.readline().split())

arr=list(map(int,sys.stdin.readline().split()))
arr.sort()

isused=[0]*n
arr2=[]

def nm9():
    if len(arr2)==m:
        print(*arr2)
        return
    remember=0
    for i in range(n):
        if isused[i]==0 and remember!=arr[i]:
            isused[i]=1
            arr2.append(arr[i])
            remember=arr[i]
            nm9()
            isused[i]=0
            arr2.pop()

nm9()