import sys
sys.setrecursionlimit(10**6)
n,m=map(int,sys.stdin.readline().split())

isused=[0]*n
arr=[]

def nm3(k):
    if k==m:
        print(*arr)
        return
    for i in range(n):
        arr.append(i+1)
        nm3(k+1)
        arr.pop()

nm3(0)