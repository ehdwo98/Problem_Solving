def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    for i in range(len(citations)):
        p=citations[i]
        if p<i+1:
            return i
        elif p==i+1:
            return i+1
    return len(citations)