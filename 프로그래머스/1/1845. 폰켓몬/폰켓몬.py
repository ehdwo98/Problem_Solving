def solution(nums):
    answer = 0
    dic=dict()
    for num in nums:
        if num not in dic:
            dic[num]=0
        dic[num]+=1
    l=len(list(dic.items()))
    answer=l if l<len(nums)//2 else len(nums)//2
    return answer