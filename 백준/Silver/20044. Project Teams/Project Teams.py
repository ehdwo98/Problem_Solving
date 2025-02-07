import sys
input=sys.stdin.readline

n=int(input())
scores=sorted(list(map(int,input().split())))
ans=[]
for i in range(n):
    ans.append(scores[i]+scores[2*n-1-i])
print(min(ans))