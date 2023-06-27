def solution(answers):
    answer = []
    n=len(answers)
    cnt1,cnt2,cnt3=0,0,0
    arr1=[1,2,3,4,5]
    arr2=[2, 1, 2, 3, 2, 4, 2, 5]
    arr3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(n):
        if answers[i]==arr1[i%5]:
            cnt1+=1
        if answers[i]==arr2[i%8]:
            cnt2+=1
        if answers[i]==arr3[i%10]:
            cnt3+=1
    score=[cnt1,cnt2,cnt3]
    for idx, s in enumerate(score):
        if s==max(score):
            answer.append(idx+1)
    
    return answer