from collections import defaultdict
import sys
input=sys.stdin.readline

n=int(input())

arr=list(map(int,input().split()))

s,e=0,0
cnt=0
dic=defaultdict(int)

ans=0
while e<n:
    if dic[arr[e]]==0:
        cnt+=1
    dic[arr[e]]+=1

    while cnt>2:
        dic[arr[s]]-=1
        if dic[arr[s]]==0:
            cnt-=1
        s+=1
    ans=max(ans,e-s+1)
    e+=1

print(ans)