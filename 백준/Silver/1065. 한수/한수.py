n=int(input())
ans=0
for i in range(1,n+1):
   tmp=list(map(int,str(i)))
   if len(tmp)>1:
      dif=tmp[1]-tmp[0]
      c=1
      for j in range(len(tmp)-1):
         if tmp[j+1]-tmp[j]!=dif:
            c=0
      if c:
         ans+=1
   else:
      ans+=1
print(ans)