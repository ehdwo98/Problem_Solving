import sys
input=sys.stdin.readline

print(format(int('0o'+input().rstrip(),8),'b'))