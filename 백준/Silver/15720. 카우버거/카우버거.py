import sys
input=sys.stdin.readline

b,c,d=map(int,input().split())
s=min(b,c,d)
arr1=sorted(list(map(int,input().split())),reverse=True)
arr2=sorted(list(map(int,input().split())),reverse=True)
arr3=sorted(list(map(int,input().split())),reverse=True)
# print(arr1,arr2,arr3)
sum1=sum(arr1)+sum(arr2)+sum(arr3)
sum2=0
for i in range(s):
    res=(arr1[i]+arr2[i]+arr3[i])
    sum2+=int(res*0.1)
print(sum1)
print(sum1-sum2)