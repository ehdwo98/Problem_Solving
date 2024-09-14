l=int(input())

def custom(x):
   return ord(x)-96

arr=list(map(custom,input().rstrip()))

# print(arr)

r,M=31,1234567891
ans=0
for i in range(l):
   ans+=(arr[i]*(r**i))%M

print(ans)