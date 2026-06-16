def solution(nums):
    answer = 0
    dic=dict()
    for num in nums:
        if num not in dic:
            dic[num]=0
        dic[num]+=1
    l=len(dic.keys())
    if l>len(nums)//2:
        return len(nums)//2
    else:
        return l
