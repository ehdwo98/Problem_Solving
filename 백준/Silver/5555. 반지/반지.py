import sys
input=sys.stdin.readline

arr=list(input().rstrip())
ans=0
n=int(input())
for _ in range(n):
    res=list(input().rstrip())
    for _ in range(len(res)):
        # print(res)
        c=0
        for i in range(len(res)-len(arr)+1):
            if res[i:i+len(arr)]==arr:
                # print(res[i:i+len(arr)])
                ans+=1
                c=1
                break
        if c:
            break
        p=res.pop(0)
        res.append(p)
print(ans)