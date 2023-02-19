N=int(input())
words=[list(input())for _ in range(N)]
#print(words)

global cnt
cnt=0

for i in words:
    error=0
    for j in range(len(i)-1):
        if i[j]!=i[j+1]:
            new=i[j+1:]
            if new.count(i[j])>0:
                error+=1
    if error==0:
        cnt+=1
print(cnt)