import sys
input=sys.stdin.readline

n=int(input())

arr=list(list(map(int,input().split())) for _ in range(n))
arr.sort(key=lambda x:[x[1],x[0]])

cnt,t=0,0
for i in range(n):
    s,e=arr[i]
    if t<=s:
        t=e
        cnt+=1

print(cnt)