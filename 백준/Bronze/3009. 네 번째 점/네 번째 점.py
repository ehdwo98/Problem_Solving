import sys
input=sys.stdin.readline

arr=list(list(map(int,input().split()))for _ in range(3))
dic=dict()
dic2=dict()
for a,b in arr:
    if a not in dic:
        dic[a]=1
    else:
        dic[a]+=1
    if b not in dic2:
        dic2[b]=1
    else:
        dic2[b]+=1

for k,v in dic.items():
    if v==1:
        print(k,end=' ')
for k,v in dic2.items():
    if v==1:
        print(k)