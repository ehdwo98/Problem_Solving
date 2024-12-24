import sys
input=sys.stdin.readline

arr=input().rstrip()
n=len(arr)

if n%2==0:
    s=n//2
else:
    s=n//2+1

ans=[]
for i in range(n//2,n):
    arr1=arr[:i][::-1]
    mid=arr[i]
    arr2=arr[i+1:]
    c=1
    for j in range(len(arr2)):
        if arr2[j]!=arr1[j]:
            c=0
    if c:
        res=len(arr1)*2+1
        ans.append(res)
        break

for i in range(s,n):
    arr1=arr[:i][::-1]
    arr3=arr[i:]
    c=1
    for j in range(len(arr3)):
        if arr3[j]!=arr1[j]:
            c=0
    if c:
        res=len(arr1)*2
        ans.append(res)
        break

print(min(ans))