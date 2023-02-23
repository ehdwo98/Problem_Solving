N=int(input())
#print(N)

data_list=[]
for _  in range(N):
    data_list.append(input())

data_list=list(set(data_list))

for index in range(len(data_list)) : 
    data_len = len(data_list[index])
    data_list[index] = (data_list[index], data_len)

data_list.sort(key = lambda x :(x[1], x[0]))

for i in data_list:
    print(i[0])
