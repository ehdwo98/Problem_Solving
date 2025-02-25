import sys
input=sys.stdin.readline

n=int(input())
ans=0
arr=list([0]*100 for _ in range(100))
for _ in range(n):
    x,y=map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j]=1

for i in range(100):
    ans+=sum(arr[i])
print(ans)