import sys
input=sys.stdin.readline

arr=list(input().rstrip().split('.'))

ans=''
for a in arr:
    if len(a)==0:
        ans+='.'
        continue
    if len(a)%2!=0:
        print(-1)
        exit(0)
    x,y=divmod(len(a),4)
    ans+=('AAAA'*x+'BB'*(y//2))
    ans+='.'
print(ans[:-1])