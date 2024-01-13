while 1:
    i=input()
    n=int(i)
    if n==0:
        break
    c=int(i[::-1])
    if n==c:
        print("yes")
    else:
        print("no")