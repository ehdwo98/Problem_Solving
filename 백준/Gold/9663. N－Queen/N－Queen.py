n=int(input())

isused1=[0]*n
isused2=[0]*(2*n-1)
isused3=[0]*(2*n-1)

cnt=0

def nqueen(k):
    global cnt
    if k==n:
        cnt+=1
        return
    for i in range(n):#y
        if isused1[i]==0 and isused2[i+k]==0 and isused3[k-i+n-1]==0:
            isused1[i],isused2[i+k],isused3[k-i+n-1]=1,1,1
            nqueen(k+1)
            isused1[i],isused2[i+k],isused3[k-i+n-1]=0,0,0
        else:
            continue

nqueen(0)

print(cnt)