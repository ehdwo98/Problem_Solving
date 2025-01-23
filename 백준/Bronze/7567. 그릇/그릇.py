import sys
input=sys.stdin.readline

arr=input().rstrip()
ans=10
for i in range(1,len(arr)):
    if arr[i-1]!=arr[i]:
        ans+=10
    else:
        ans+=5
print(ans)