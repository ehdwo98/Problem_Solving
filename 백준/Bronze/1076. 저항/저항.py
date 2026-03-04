ans=''
for i in range(3):
    c=input().rstrip()
    if c=='black':
        if i==2:
            ans=int(ans)*10**0
        else:
            ans+='0'
    elif c=='brown':
        if i==2:
            ans=int(ans)*10**1
        else:
            ans+='1'
    elif c=='red':
        if i==2:
            ans=int(ans)*10**2
        else:
            ans+='2'
    elif c=='orange':
        if i==2:
            ans=int(ans)*10**3
        else:
            ans+='3'
    elif c=='yellow':
        if i==2:
            ans=int(ans)*10**4
        else:
            ans+='4'
    elif c=='green':
        if i==2:
            ans=int(ans)*10**5
        else:
            ans+='5'
    elif c=='blue':
        if i==2:
            ans=int(ans)*10**6
        else:
            ans+='6'
    elif c=='violet':
        if i==2:
            ans=int(ans)*10**7
        else:
            ans+='7'
    elif c=='grey':
        if i==2:
            ans=int(ans)*10**8
        else:
            ans+='8'
    elif c=='white':
        if i==2:
            ans=int(ans)*10**9
        else:
            ans+='9'
print(ans)