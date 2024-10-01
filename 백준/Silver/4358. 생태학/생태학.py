import sys
input=sys.stdin.readline

dic=dict()
cnt=0
while True:
   try:
      tmp=input().rstrip()
      if not tmp:
         break
      if tmp not in dic:
         dic[tmp]=1
      else:
         dic[tmp]+=1
      cnt+=1
   except EOFError:
      break

dic2=dict(sorted(dic.items()))

for k,v in dic2.items():
   print(f'{k} {(v/cnt)*100:.4f}')