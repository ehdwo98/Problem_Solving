import sys
input=sys.stdin.readline

s=input().rstrip()
e=input().rstrip()

stack=[]
for i in range(len(s)):
   stack.append(s[i])
   if ''.join(stack[-len(e):])==e:
      for _ in range(len(e)):
         stack.pop()

if not stack:
   print('FRULA')
else:
   print(''.join(stack))