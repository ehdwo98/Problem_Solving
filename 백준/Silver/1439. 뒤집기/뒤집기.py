s=list(input().rstrip())

p=s[0]

ans=0
for i in range(len(s)):
   if p!=s[i]:
      ans+=1
      p=s[i]

print((ans+1)//2)