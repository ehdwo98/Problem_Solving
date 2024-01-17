from sys import stdin

input=stdin.readline

n=int(input())
q=[]
for _ in range(n):
    arr=list(input().split())
    
    if arr[0]=='push':
        c,n=arr
        q.append(n)
    elif arr[0]=='pop':
        if len(q)==0:
            print(-1)
        else:
            p=q.pop(0)
            print(p)
    elif arr[0]=='size':
        print(len(q))
    elif arr[0]=='empty':
        if len(q)==0:
            print('1')
        else:
            print('0')
    elif arr[0]=='front':
        if len(q)==0:
            print('-1')
        else:
            print(q[0])
    elif arr[0]=='back':
        if len(q)==0:
            print('-1')
        else:
            print(q[-1])