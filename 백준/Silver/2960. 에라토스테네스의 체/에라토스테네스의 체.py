from collections import deque
n,k=map(int,input().split())

arr=[x for x in range(2,n+1)]
q=deque(arr)
while q:
    p=q[0]
    for i in range(1,n//p+1):
        if p*i in q:
            k-=1
            if k==0:
                print(p*i)
                break
            q.remove(p*i)