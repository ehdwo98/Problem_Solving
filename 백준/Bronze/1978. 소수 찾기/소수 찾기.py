n=int(input())
arr=list(map(int,input().split()))
cnt=0

def check(a):
    if a>1:
        for i in range(2,a):
            if a%i==0:
                return 0
        return 1
    else:
        return 0

for a in arr:
    if check(a)==1:
        cnt+=1
        
print(cnt)