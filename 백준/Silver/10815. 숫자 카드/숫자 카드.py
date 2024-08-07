import bisect

n=int(input())
arr1=list(map(int,input().split()))
arr1.sort()


m=int(input())
arr2=list(map(int,input().split()))

for a in arr2:
   res=bisect.bisect(arr1,a)-bisect.bisect_left(arr1,a)
   if res!=0:
      print(1, end=' ')
   else:
      print(0, end=' ')