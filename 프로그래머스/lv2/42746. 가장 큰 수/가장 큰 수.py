def solution(numbers):
    numbers=list(map(str,numbers))
    numbers.sort(reverse=True, key = lambda x : (x*4)[:4])
    answer=''.join(numbers)
    if answer[0]=='0':
        return '0'
    else:
        return answer