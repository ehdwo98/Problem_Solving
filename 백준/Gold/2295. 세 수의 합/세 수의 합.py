#기존 풀이 -> 런타임에러
""""
import sys
from itertools import combinations
input = sys.stdin.readline
N=int(input())
arr=set()
for i in range(N):
    a=int(input())
    arr.add(a)
    
Max=0
comb=list(combinations(arr,3))
for i in comb:
    tmp=sum(i)
    if tmp in arr:
        Max=max(Max,tmp)
print(Max)
"""
import sys
input = sys.stdin.readline

N=int(input())
arr=set()

for i in range(N):
    a=int(input())
    arr.add(a)
sums=set()
for i in arr:
    for j in arr:
        sums.add(i+j)
ans=[]
for i in arr:
    for j in arr:
        if (i-j)in sums:
            ans.append(i)
ans.sort()
print(ans[-1])