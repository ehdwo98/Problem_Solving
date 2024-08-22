import bisect

n,m=map(int,input().split())

arr1=list(input().rstrip() for _ in range(n))
arr2=sorted(list(input().rstrip() for _ in range(m)))

ans=[]
for a in arr1:
   if bisect.bisect_right(arr2,a)-bisect.bisect_left(arr2,a)!=0:
      ans.append(a)

ans.sort()
print(len(ans))
for a in ans:
   print(a)