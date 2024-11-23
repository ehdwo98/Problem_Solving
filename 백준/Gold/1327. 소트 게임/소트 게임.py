from collections import deque

n,k=map(int,input().split())
arr=input().split()
visit=dict()
arr_sort=sorted(arr)

q=deque()
q.append([arr,0])
while q:
    a,cnt=q.popleft()
    if a==arr_sort:
        print(cnt)
        exit(0)
    for i in range(n-k+1):
        tmp=a[i:i+k][::-1]
        arr2=a[:i]+tmp+a[i+k:]
        res=''.join(arr2)
        if res not in visit:
            visit[res]=1
            q.append([arr2,cnt+1])
print(-1)