def solution(triangle):
    n=len(triangle)
    dp=list([0]*(i+1) for i in range(n))
    # print(dp)

    # dp[i][j]=triangle[i][j]+max(dp[i-1][j],dp[i-1][j+1])
    # 7
    # 10 15
    # 23 16 15
    # 25 30 20 19
    
    dp[0][0]=triangle[0][0]

    for i in range(1,n):
        for j in range(i+1):
            if j==0:
                dp[i][j]=triangle[i][j]+dp[i-1][0]
            elif j==i:
                dp[i][j]=triangle[i][j]+dp[i-1][j-1]
            else:
                dp[i][j]=triangle[i][j]+max(dp[i-1][j],dp[i-1][j-1])
    
    # print(dp)
    answer=max(dp[n-1])
    
    return answer