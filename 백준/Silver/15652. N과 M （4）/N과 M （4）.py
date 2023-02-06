N,M=map(int,input().split())

array=[i for i in range(1,N+1)]

def combi(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combi(array[i:], r-1):
                yield [array[i]] + next

for i in combi(array,M):
    print(" ".join(map(str,i)))