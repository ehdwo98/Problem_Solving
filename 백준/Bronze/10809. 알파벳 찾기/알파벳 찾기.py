from collections import Counter
import sys
input=sys.stdin.readline

s=input().rstrip()
arr=list(s)

ans=[]
for i in range(ord('a'),ord('z')+1,1):
    if chr(i) in arr:
        ans.append(arr.index(chr(i)))
    else:
        ans.append(-1)

for a in ans:
    print(a,end=' ')