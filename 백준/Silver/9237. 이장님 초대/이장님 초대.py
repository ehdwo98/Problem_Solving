import sys
input=sys.stdin.readline

n=int(input())
arr=sorted(list(map(int,input().split())),reverse=True)
ans=list()
for i in range(n):
    ans.append(2+arr[i]+i)

print(max(ans))