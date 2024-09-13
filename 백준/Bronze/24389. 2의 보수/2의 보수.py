n=int(input())

n=bin(n)[2:].zfill(32)
# print(n)

c=['0']*32
for i in range(len(n)):
   if n[i]=='0':
      c[i]='1'

res=bin(int(''.join(c),2)+1)[2:]
# print(res)

ans=0
for i in range(32):
   if n[i]!=res[i]:
      ans+=1

print(ans)