n=list(map(int,input().split()))
sum=0
for a in n:
    sum+=a**2

print(sum%10)