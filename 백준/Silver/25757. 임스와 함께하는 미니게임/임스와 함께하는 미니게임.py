import sys
input=sys.stdin.readline

n,c=input().split()
n=int(n)

dic=dict()
for i in range(n):
   tmp=input().rstrip()
   dic[tmp]=1

l=len(dic.keys())
if c=='Y':
   print(l//1)
elif c=='F':
   print(l//2)
else:
   print(l//3)