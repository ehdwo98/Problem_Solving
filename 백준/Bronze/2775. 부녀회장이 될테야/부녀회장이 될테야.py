t=int(input())

for _ in range(t):
    k=int(input())
    n=int(input())
    arr=[[0]*n for _ in range(k+1)]
    sum=0
    for i in range(k+1):
        for j in range(n):
            if i==0:
                arr[i][j]=j+1
            else:
                for l in range(j+1):
                    sum+=arr[i-1][l]
                arr[i][j]=sum
                sum=0

    print(arr[k][n-1])
