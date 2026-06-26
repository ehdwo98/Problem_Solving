def solution(numbers, target):
    answer=0
    def dfs(num,tar):
        nonlocal answer
        if tar==len(numbers) and num==target:
            answer+=1
        if tar>=len(numbers):
            return
        dfs(num+numbers[tar],tar+1)
        dfs(num-numbers[tar],tar+1)
    dfs(0,0)
    return answer