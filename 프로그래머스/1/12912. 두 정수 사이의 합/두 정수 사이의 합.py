def solution(a, b):
    if b>=a:
        answer = sum(list(i for i in range(a,b+1)))
    else:
        answer = sum(list(i for i in range(b,a+1)))
        
    return answer