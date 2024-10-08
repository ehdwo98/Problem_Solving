import sys
input=sys.stdin.readline

S=input().rstrip()

stack=[]
ans=''
c=0
for s in S:
   if s=='<':
      for _ in range(len(stack)):
         ans+=stack.pop()
      c=1
   stack.append(s)
   if s=='>':
      for _ in range(len(stack)):
         ans+=stack.pop(0)
      c=0
   if s==' 'and c==0:
      for i in range(len(stack)):
         if i==0:
            stack.pop()
            continue
         ans+=stack.pop()
      ans+=' '

if stack:
   for _ in range(len(stack)):
      ans+=stack.pop()

print(ans)