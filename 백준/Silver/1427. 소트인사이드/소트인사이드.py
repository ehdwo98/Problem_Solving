import sys
input=sys.stdin.readline

n=sorted(map(int,list(input().rstrip())),reverse=True)

print(''.join(map(str,n)))