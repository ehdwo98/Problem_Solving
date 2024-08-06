import sys
import bisect
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
arr2=sorted(list(set(arr)))
for a in arr:
   pos=bisect.bisect_left(arr2,a)
   print(pos, end=' ')