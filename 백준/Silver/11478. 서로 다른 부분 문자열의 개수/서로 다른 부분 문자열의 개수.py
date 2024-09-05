S=input().rstrip()
n=len(S)

arr=[]
for i in range(n):
   for j in range(i,n):
      arr.append(S[i:j+1])

print(len(set(arr)))