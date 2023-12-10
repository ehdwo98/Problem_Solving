def solution(numbers, target):
    answer = 0
    def dfs(x,n):
        if n==len(numbers):
            if x==target:
                return 1
            else:
                return 0
        return dfs(x+numbers[n],n+1)+dfs(x-numbers[n],n+1)
        
    answer=dfs(0,0)

    return answer