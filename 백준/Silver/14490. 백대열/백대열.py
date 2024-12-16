import sys
input=sys.stdin.readline
from math import gcd

n,m=map(int,input().split(':'))

l=gcd(n,m)
print(n//l,end=':')
print(m//l)