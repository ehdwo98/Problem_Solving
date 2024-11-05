import heapq
import sys
input=sys.stdin.readline

n=int(input())

arr=[]
for _ in range(n):
    tmp=int(input())
    if tmp:
        heapq.heappush(arr,-tmp)
    else:
        if len(arr):
            ans=(-heapq.heappop(arr))
            print(ans)
        else:
            print(0)