import sys
input=sys.stdin.readline

arr=[_ for _ in range(1,21)]

for _ in range(10):
    a,b=map(int,input().split())
    tmp=arr[a-1:b][::-1]
    arr[a-1:b]=tmp

print(*arr)