n=int(input())
res=1
arr=[]
stack=[]
for _ in range(n):
    num=int(input())
    while res<=num:
        stack.append(res)
        arr.append('+')
        res+=1
    if stack[-1]==num:
        stack.pop()
        arr.append('-')
    else:
        print('NO')
        exit(0)

for a in arr:
    print(a)