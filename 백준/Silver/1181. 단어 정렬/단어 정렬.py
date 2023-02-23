N=int(input())
#print(N)

words=[]
for _  in range(N):
    words.append(input())

words=set(words)
words=list(words)


words.sort()
words.sort(key=len)

for i in words:
    print(i)