import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))

arr=sorted(arr,reverse=True)
for a in arr:
    print(a)