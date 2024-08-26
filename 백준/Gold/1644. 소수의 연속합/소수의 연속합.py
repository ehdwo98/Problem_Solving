n=int(input())

is_prime=[0,0]+[1]*(n-1)
arr=[]
for i in range(2,n+1):
   if is_prime[i]:
      arr.append(i)
      for j in range(i*2,n+1,i):
         is_prime[j]=0

arr_n=len(arr)

s,e=0,0
ans=0
while e<arr_n:
   tmp=arr[s:e+1]
   if sum(tmp)>=n:
      s+=1
      if sum(tmp)==n:
         ans+=1
   else:
      e+=1

print(ans)