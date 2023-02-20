X=int(input())

line=1
while X>line:
    X-=line
    line+=1

#print(X,line)

if line%2==0:
    i,j=X,line-X+1
else:
    i,j=line-X+1,X
    
print(i,'/',j,sep='')