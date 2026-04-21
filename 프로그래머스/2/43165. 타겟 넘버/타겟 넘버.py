ans=0
def dfs(numbers,target,cnt):
    global ans
    # print(numbers)
    if cnt==len(numbers):
        if sum(numbers)==target:
            ans+=1
        return
    dfs(numbers,target,cnt+1)
    numbers[cnt]=-numbers[cnt]
    dfs(numbers,target,cnt+1)

def solution(numbers, target):
    answer = 0
    dfs(numbers,target,0)
    return ans