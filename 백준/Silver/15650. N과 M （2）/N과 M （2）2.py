import sys
sys.setrecursionlimit(10**6)
n,m=map(int,sys.stdin.readline().split())

isused=[0]*n
arr=[]
arrs=[]

#set을 이용한 방법
def nm2(k):
    if k==m and set(arr) not in arrs:
        for i in range(m):
            print(arr[i],end=' ')
        arrs.append(set(arr))
        print()
        return
    for i in range(n):
        if isused[i]==0:
            arr.append(i+1)
            isused[i]=1
            nm2(k+1)
            isused[i]=0
            arr.pop()

nm2(0)
