import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
arr=sorted(list(map(int,input().split())))
dic=dict()
for i in range(n):
    dic[arr[i]]=1

ans=0
for i in range(n):
    if m-arr[i] in dic:
        ans+=1

print(ans//2)