import sys
from collections import Counter
import math
input=sys.stdin.readline

n=list(input().strip())

for i in range(len(n)):
    n[i]=int(n[i])

c=Counter(n)

ans=[]
for i in range(0,10):
    if i in n:
        ans.append(c[i])
    else:
        ans.append(0)
#print(ans)
ans[6]=math.ceil((ans[6]+ans[9])/2)
ans[9]=0
ans.sort(reverse=True)
print(ans[0])