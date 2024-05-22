n=int(input())

sum=1
cnt=0
if n==1:
    print(1)
    exit(0)
while 1:
    cnt+=1
    sum+=6*cnt
    if sum>=n:
        print(cnt+1)
        break