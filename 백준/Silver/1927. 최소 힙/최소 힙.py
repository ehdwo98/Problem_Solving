import heapq
import sys
input=sys.stdin.readline

M=int(input())
h=[]
for _ in range(M):
    x=int(input())
    if x!=0:
        heapq.heappush(h,x)
    else:
        try:
            ans=heapq.heappop(h)
            print(ans)
        except:
            print(0)


