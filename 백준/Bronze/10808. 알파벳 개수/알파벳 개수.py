import sys
from collections import Counter
input=sys.stdin.readline

s=list(input())
c=Counter(s)

ans=[]
for i in range(ord('a'),ord('z')+1):
    if chr(i) in s:
        ans.append(c[chr(i)])
    else:
        ans.append(0)

for a in ans:
    print(a,end=' ')