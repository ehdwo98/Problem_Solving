import sys
input=sys.stdin.readline

num=123456*2+1
arr=[x for x in range(num)]


for i in range(2,num):
    for j in range(2,int(i**(1/2)+1)):
            if i%j==0:
                arr[i]=0
                break

while 1:
    n=int(input())
    if n==0:
        break
    cnt=0
    for i in range(n+1,2*n+1):
        if arr[i]>0:
            cnt+=1
    print(cnt)