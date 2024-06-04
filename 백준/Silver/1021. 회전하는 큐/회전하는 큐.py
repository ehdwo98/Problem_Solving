from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
find=list(map(int,input().split()))

q=deque()
for i in range(1,n+1):
    q.append(i)
#print(q)
cnt=0
for f in find:
    while 1:
        if q[0]==f:
            q.popleft()
            break
        else:
            if q.index(f)<(len(q)/2):
                q.append(q.popleft())
                cnt+=1
            else:
                q.appendleft(q.pop())
                cnt+=1

print(cnt)