import sys
input=sys.stdin.readline

n=int(input())

for _ in range(n):
    tmp=list(map(int,input().split()))
    Ti,arr=tmp[0],tmp[1:]
    dic=dict()
    for a in arr:
        if a not in dic:
            dic[a]=1
        else:
            dic[a]+=1
    res=sorted(dic.items(),key=lambda x:-x[1])
    if res[0][1]>Ti//2:
        print(res[0][0])
    else:
        print('SYJKGW')