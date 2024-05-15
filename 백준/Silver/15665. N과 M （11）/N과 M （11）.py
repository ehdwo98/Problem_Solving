import sys
sys.setrecursionlimit(10**6)
n,m=map(int,sys.stdin.readline().split())

arr=list(map(int,sys.stdin.readline().split()))
arr.sort()

arr2=[]

def nm10():
    if len(arr2)==m:
        print(*arr2)
        return
    remember=0
    for i in range(n):
        if remember!=arr[i]:
            arr2.append(arr[i])
            remember=arr[i]
            nm10()
            arr2.pop()

nm10()