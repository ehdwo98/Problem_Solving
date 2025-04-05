import sys
input=sys.stdin.readline

arr=input().rstrip()

ans=list()
for i in range(1,len(arr)-1):
    for j in range(i+1,len(arr)):
        a=arr[:i]
        b=arr[i:j]
        c=arr[j:]
        # print(a,b,c)
        res=a[::-1]+b[::-1]+c[::-1]
        ans.append(res)
ans.sort()
# print(ans)
print(ans[0])