n=int(input())

arr=list(list(input().rstrip())for _ in range(n))

for i in range(len(arr[0])):
    c=0
    for j in range(n):
        res=arr[j][i]
        if res!=arr[0][i]:
            c=1
    if c:
        print('?',end='')
    else:
        print(arr[0][i],end='')