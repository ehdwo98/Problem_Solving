a,b=map(int,input().split())


arr=[]
for i in range(1,100):
   for _ in range(i):
      if len(arr)>b:
         break
      arr.append(i)

arr_slice=arr[a-1:b]
print(sum(arr_slice))