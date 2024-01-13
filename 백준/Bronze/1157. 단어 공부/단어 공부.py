from collections import Counter
i=input().upper()
words=list(i)
words=Counter(words)

if len(words)==1:
    print(i[0])
else:
    top=words.most_common(2)
    if top[0][1]==top[1][1]:
        print('?')
    else:
        print(top[0][0])
