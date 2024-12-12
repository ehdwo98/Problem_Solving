import sys
input=sys.stdin.readline

n=int(input())
arr1,arr2=list(),list()
ans=0
for i in range(n):
    res=int(input())
    if res>1:
        arr1.append(res)
    elif res<1:
        arr2.append(res)
    else:
        ans+=res

arr1=sorted(arr1,reverse=True)
arr2=sorted(arr2)

for i in range(0,len(arr1),2):
    if i+1>=len(arr1):
        ans+=arr1[i]
    else:
        ans+=arr1[i]*arr1[i+1]

for i in range(0,len(arr2),2):
    if i+1>=len(arr2):
        ans+=arr2[i]
    else:
        ans+=arr2[i]*arr2[i+1]
print(ans)