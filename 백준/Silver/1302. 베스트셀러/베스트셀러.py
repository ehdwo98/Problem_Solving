n=int(input())

dic=dict()
for _ in range(n):
   title=input().rstrip()
   if title in dic:
      dic[title]+=1
   else:
      dic[title]=1

arr=list(dic.items())
arr.sort(key=lambda x:(-x[1],x[0]))
print(arr[0][0])