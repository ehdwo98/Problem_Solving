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
    for i in range(n):# i:열 -> 가로, k:행 -> 세로
        if isused1[i]==0 and isused2[i+k]==0 and isused3[k-i+n-1]==0:
            #열 방향, 왼쪽 아래에서 오른쪽 위로 가는 대각선 방향, 오른쪽 아래에서 왼쪽 위로 가는 방향 
            isused1[i],isused2[i+k],isused3[k-i+n-1]=1,1,1
            nqueen(k+1)
            isused1[i],isused2[i+k],isused3[k-i+n-1]=0,0,0
        else:
            continue

nqueen(0)

print(cnt)
