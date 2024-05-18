n=int(input())
c=1
for i in range(n):
    list_i=list(map(int,str(i)))
    if i+sum(list_i)==n:
        print(i)
        c=0
        break
if c:
    print(0)