from sys import stdin

input=stdin.readline

n=int(input())
stack=[]
for _ in range(n):
    arr=list(input().split())
    
    if arr[0]=='push':
        c,n=arr
        stack.append(n)
    elif arr[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            p=stack.pop()
            print(p)
    elif arr[0]=='size':
        print(len(stack))
    elif arr[0]=='empty':
        if len(stack)==0:
            print('1')
        else:
            print('0')
    elif arr[0]=='top':
        if len(stack)==0:
            print('-1')
        else:
            print(stack[-1])