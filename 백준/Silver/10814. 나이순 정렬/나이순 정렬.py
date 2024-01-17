n=int(input())
arr=[]
for _ in range(n):
    age,name=input().split()
    # print(age,name)
    age=int(age)
    arr.append([age,name])
    
arr.sort(key=lambda x:(x[0]))

for a in arr:
    print(*a)