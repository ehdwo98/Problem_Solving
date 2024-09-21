n=int(input())

dic=dict()
for i in range(n):
   tmp=input().split('.')[1]
   if tmp not in dic:
      dic[tmp]=1
   else:
      dic[tmp]+=1

arr=sorted(list(dic.items()))
for k,v in arr:
   print(k,v)