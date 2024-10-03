import sys
input=sys.stdin.readline

n=sorted(map(int,list(input().rstrip())),reverse=True)

for i in n:
   print(i,end='')