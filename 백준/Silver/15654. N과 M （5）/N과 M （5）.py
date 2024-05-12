import sys
sys.setrecursionlimit(10**6)
n,m=map(int,sys.stdin.readline().split())

arr=list(map(int,sys.stdin.readline().split()))
arr.sort()

isused=[0]*n
arr2=[]

def nm3(k):
    if k==m:
        print(*arr2)
        return
    for i in range(n):
        if isused[i]==0:
            isused[i]=1
            arr2.append(arr[i])
            nm3(k+1)
            isused[i]=0
            arr2.pop()

nm3(0)