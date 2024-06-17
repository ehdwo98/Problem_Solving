import math
n=int(input())

arr=list(map(int,input().split()))

t,p=map(int,input().split())

sum_t=0
for a in arr:
    sum_t+=math.ceil(a/t)

print(sum_t)

a,b=divmod(n,p)
print(a,b)