import sys

n,m=map(int,sys.stdin.readline().split())

isused=[0]*n
arr=[]

def nm2(k,idx):
    if k==m:
        print(*arr)
        return
    for i in range(idx,n):
        if isused[i]==0:
            arr.append(i+1)
            isused[i]=1
            nm2(k+1,i+1)
            isused[i]=0
            arr.pop()

nm2(0,0)