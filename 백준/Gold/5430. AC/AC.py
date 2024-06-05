from collections import deque
import sys
input=sys.stdin.readline

def dq():
    q=deque(arr)
    f=0
    for c in p:
        if c=='R':
            if len(q)==0:
                continue
            else:
                if f==0:
                    f=1
                else:
                    f=0
        elif c=='D':
            if len(q)==0:
                print("error")
                return
            else:
                if f:
                    q.pop()
                else:
                    q.popleft()
    if f:
        q.reverse()
        print('['+','.join(list(map(str,q)))+']')
    else:
        print('['+','.join(list(map(str,q)))+']')
    return

t=int(input())
while t:
    p=list(input().strip())
    n=int(input())
    arr=input().strip()[1:-1]
    if len(arr)!=0:
        arr=list(map(int,arr.split(',')))
    #print(arr)
    dq()
    t-=1