import sys
sys.setrecursionlimit(10**6)
n,m=map(int,sys.stdin.readline().split())

arr=list(map(int,sys.stdin.readline().split()))
arr.sort()
isused=[0]*n
arr2=[]
arr3=[]
tmp=[]

# 튜플을 이용해서 풀기
def nm9(k):
    if k==m:
        arr3.append(tuple(arr2))
        return
    for i in range(n):
        if isused[i]==0:
            isused[i]=1
            arr2.append(arr[i])
            nm9(k+1)
            isused[i]=0
            arr2.pop()

nm9(0)

# set을 이용해서 중복제거
arr3=list(set(arr3))
arr3.sort()
for a in arr3:
    print(*a)
