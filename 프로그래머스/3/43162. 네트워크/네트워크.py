def find(parents,num):
    if parents[num]==num:
        return num
    return find(parents,parents[num])
def solution(n, computers):
    answer = 0
    parents=list(x for x in range(n))
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1:
                a=find(parents,i)
                b=find(parents,j)
                print(a,b)
                if a<b:
                    parents[b]=a
                else:
                    parents[a]=b
                print(parents)
    tmp=list(find(parents,i) for i in range(n))
    print(tmp)
    answer=len(set(list(find(parents,i) for i in range(n))))
    return answer