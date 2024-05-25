from collections import Counter
import sys
input=sys.stdin.readline

n=int(input())

arr=[]
for _ in range(n):
    p=int(input())
    arr.append(p)
# 1
arr.sort()
print(round(sum(arr)/n))
# 2
print(arr[n//2])

# 3
arr2=Counter(arr)
if n==1:
    print(arr[0])
else:
    mc=arr2.most_common(2)
    if mc[0][1]==mc[1][1]:
        print(mc[1][0])
    else:
        print(mc[0][0])

# 4
if n==1:
    print(0)
else:
    print(arr[-1]-arr[0])