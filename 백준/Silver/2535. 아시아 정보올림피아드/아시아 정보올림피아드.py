import sys
input=sys.stdin.readline

n=int(input())

arr=sorted(list(list(map(int,input().split())) for _ in range(n)),key=lambda x:-x[2])

c=[2]*(n+1)
ans=1
for i in range(n):
    if c[arr[i][0]]>0 and ans<=3:
       print(arr[i][0],arr[i][1])
       c[arr[i][0]]-=1
       ans+=1