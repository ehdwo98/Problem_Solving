import sys
input=sys.stdin.readline

n=int(input())

room=list(list(input().rstrip()) for _ in range(n))

ans=0
for i in range(n):
    cnt=0
    for j in range(n):
        if room[i][j]=='.':
            cnt+=1
        if room[i][j]=='X' or j==n-1:
            if cnt>=2:
                ans+=1
            cnt=0

print(ans,end=' ')

ans1=0
for j in range(n):
    cnt=0
    for i in range(n):
        if room[i][j]=='.':
            cnt+=1
        if room[i][j]=='X' or i==n-1:
            if cnt>=2:
                ans1+=1
            cnt=0
print(ans1)