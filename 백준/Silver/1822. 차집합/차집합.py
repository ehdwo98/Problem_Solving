import bisect

a,b=map(int,input().split())
arr1=list(map(int,input().split()))
arr1.sort()

arr2=list(map(int,input().split()))
arr2.sort()

cnt=0
ans=[]
for a in arr1:
   if bisect.bisect_right(arr2,a)-bisect.bisect_left(arr2,a)==0:
      cnt+=1
      ans.append(a)

if cnt:
   print(cnt)
   print(*ans)
else:
   print(0)