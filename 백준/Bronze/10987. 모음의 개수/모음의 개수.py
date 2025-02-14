import sys
input=sys.stdin.readline

arr=input().rstrip()
ans=0
for i in ['a','e','i','o','u']:
    ans+=arr.count(i)
print(ans)