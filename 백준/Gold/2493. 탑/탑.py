n=int(input())
arr=list(map(int,input().split()))
ans=[0]*n
stack=[]
for i in range(n-1,-1,-1):
    while stack:
        idx = stack[-1]
        if arr[i] < arr[idx]: break
        ans[idx] = i+1

        stack.pop()

    stack.append(i)

print(*ans)