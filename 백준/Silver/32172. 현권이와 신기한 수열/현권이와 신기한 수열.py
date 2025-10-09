import sys
input=sys.stdin.readline
from collections import defaultdict

n=int(input())

dic=dict()
dic[0]=0

dic2=defaultdict(int)
dic2[0]=1
for i in range(1,n+1):
    tmp=dic[i-1]-i
    if tmp<0 or dic2[tmp]==1:
        tmp=dic[i-1]+i
    dic[i]=tmp
    dic2[tmp]=1

print(dic[n])