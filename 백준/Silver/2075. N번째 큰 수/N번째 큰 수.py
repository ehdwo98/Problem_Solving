import sys
input=sys.stdin.readline
import heapq

n=int(input())
arr=list()
for _ in range(n):
    tmp=list(map(int,input().split()))
    if not arr:
        for t in tmp:
            heapq.heappush(arr,t)
    else:
        for t in tmp:
            if arr[0] < t:
                heapq.heappush(arr,t)
                heapq.heappop(arr)
print(arr[0])