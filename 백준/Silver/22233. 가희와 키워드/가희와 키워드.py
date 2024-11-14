import sys
input=sys.stdin.readline

n,m=map(int,input().split())

dic=dict()
ans=0
for _ in range(n):
    tmp=input().rstrip()
    dic[tmp]=1
    ans+=1

for _ in range(m):
    tmp=list(input().rstrip().split(','))
    for t in tmp:
        if t in dic:
            if dic[t]==1:
                dic[t]=0
                ans-=1
    print(ans)