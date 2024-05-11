import sys
sys.setrecursionlimit(10**6)
n,m=map(int,sys.stdin.readline().split())

isused=[0]*10
arr=[]

#idx를 통해 [x,y]에서 항상 x<y를 만족시키게 만들어 조합을 생성
def nm2(k,idx):
    if k==m:
        print(*arr)
        return
    for i in range(idx,n):
        if isused[i]==0:
            arr.append(i+1)
            isused[i]=1
            nm2(k+1,i+1)
            isused[i]=0
            arr.pop()

nm2(0,0)
