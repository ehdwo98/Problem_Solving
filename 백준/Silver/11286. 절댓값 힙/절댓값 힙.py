import heapq
import sys
input=sys.stdin.readline

M=int(input())
h=[]
for _ in range(M):
    x=int(input())
    if x!=0:
        heapq.heappush(h,[abs(x),x])
    else:
        try:
            ans=heapq.heappop(h)[1]
            print(ans)
        except:
            print(0)