import sys
input=sys.stdin.readline
import math
n=int(input())
arr=sorted(list(map(int,input().split())))
# print(arr)

s,e=0,n-1
mx=math.inf
while s<e:
    res=arr[s]+arr[e]
    if abs(res)<abs(mx):
        mx=res
        l,r=s,e
    if res>0:
        e-=1
    else:
        s+=1
print(arr[l],arr[r])