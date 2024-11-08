import heapq
import sys
input=sys.stdin.readline


n=int(input())

arr=[]

for _ in range(n):
    heapq.heappush(arr,int(input()))

ans=0

while len(arr)>1:
    a=heapq.heappop(arr)
    b=heapq.heappop(arr)
    tmp=a+b
    ans+=tmp
    heapq.heappush(arr,tmp)

print(ans)