import sys
input=sys.stdin.readline

n=int(input())
arr=list()
for _ in range(n):
    name,d,m,y=input().rstrip().split()
    d=int(d)
    m=int(m)
    y=int(y)
    arr.append([name,d,m,y])

arr=sorted(arr,key=lambda x:(x[3],x[2],x[1]))
print(arr[-1][0])
print(arr[0][0])