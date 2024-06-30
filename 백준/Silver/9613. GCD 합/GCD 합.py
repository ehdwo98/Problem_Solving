from itertools import combinations
from math import gcd
import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    arr=list(map(int,input().split()))
    n=arr.pop(0)
    combi=list(combinations(arr,2))
    res=[]
    for c in combi:
        a,b=c
        res.append(gcd(a,b))
    print(sum(res))