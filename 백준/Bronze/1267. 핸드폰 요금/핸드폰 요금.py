import math
n=int(input())
arr=list(map(int,input().split()))

sum1,sum2=0,0
for a in arr:
    if a%30==0:
        sum1+=(math.ceil(a/30)+1)*10
    elif a%30!=0:
        sum1+=math.ceil(a/30)*10
    if a%60==0:
        sum2+=(math.ceil(a/60)+1)*15
    elif a%60!=0:
        sum2+=math.ceil(a/60)*15

if sum1<sum2:
    print('Y',sum1)
elif sum1>sum2:
    print('M',sum2)
else:
    print('Y','M',sum1)