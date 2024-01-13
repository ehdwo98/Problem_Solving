import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
m=int(input())
test=list(map(int,input().split()))
arr=set(arr)
for t in test:
    if t in arr:
        print(1)
    else:
        print(0)