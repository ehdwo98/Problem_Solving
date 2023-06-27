def solution(answers):
    answer = []
    n=len(answers)
    cnt1,cnt2,cnt3=0,0,0
    arr=[1,2,3,4,5]
    for i in range(n):
        if answers[i]==arr[i%5]:
            cnt1+=1
    arr=[2, 1, 2, 3, 2, 4, 2, 5]
    for i in range(n):
        if answers[i]==arr[i%8]:
            cnt2+=1
    arr=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(n):
        if answers[i]==arr[i%10]:
            cnt3+=1
            
    if cnt1>cnt2:
        if cnt1>cnt3:
            answer.append(1)
        if cnt1==cnt3:
            answer.append(1)
            answer.append(3)
        if cnt1<cnt3:
            answer.append(3)
    if cnt1==cnt2:
        if cnt2>cnt3:
            answer.append(1)
            answer.append(2)
        if cnt2==cnt3:
            answer.append(1)
            answer.append(2)
            answer.append(3)
        if cnt2<cnt3:
            answer.append(3)
    if cnt1<cnt2:
        if cnt2>cnt3:
            answer.append(2)
        if cnt2==cnt3:
            answer.append(2)
            answer.append(3)
        if cnt2<cnt3:
            answer.append(3)
    return answer