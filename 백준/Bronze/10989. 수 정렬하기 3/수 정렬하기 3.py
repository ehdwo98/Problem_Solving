import sys
input=sys.stdin.readline

n=int(input())
arr=[0]*10001

for _ in range(n):
    p=int(input())
    arr[p]+=1
for i in range(1,10001):
    if arr[i]!=0:
        for j in range(arr[i]):
            print(i)