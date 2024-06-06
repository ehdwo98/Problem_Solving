from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
cnt=0
for _ in range(n):
    c=deque(input().strip())
    #print(c)
    cl=len(c)
    while len(c)>1 and cl:
        if c[0]==c[-1]:
            c.popleft()
            c.pop()
        else:
            c.appendleft(c.pop())
            cl-=1
    if len(c)==0:
        cnt+=1

print(cnt)