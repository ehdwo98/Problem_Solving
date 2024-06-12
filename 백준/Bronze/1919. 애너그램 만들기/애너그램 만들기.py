import sys
input=sys.stdin.readline

arr1=list(input().strip())
arr2=list(input().strip())

a1=[0]*26
a2=[0]*26

for a in arr1:
    idx=ord(a)-97
    a1[idx]+=1

for b in arr2:
    idx=ord(b)-97
    a2[idx]+=1

cnt=0
for i in range(26):
    cnt+=abs(a1[i]-a2[i])

print(cnt)