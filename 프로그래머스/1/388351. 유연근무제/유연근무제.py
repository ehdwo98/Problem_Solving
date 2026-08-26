def solution(schedules, timelogs, startday):
    answer = 0
    n=len(schedules)
    for cur in range(n):
        schedule=schedules[cur]
        timelog=timelogs[cur]
        cmd=0
        for i in range(7): #5,6,7,8,9,...
            j=(i+startday)%7
            if 1<=j<=5:
                tmp=int(str(schedule)[-2:])
                print(tmp)
                print(timelog[i], schedule)
                if tmp>=50:
                    if timelog[i]-schedule>50:#9:55-> 955, 10:05->1005
                        cmd=1
                        break
                else:
                    if timelog[i]-schedule>10:#9:49-> 949, 9:59->959
                        cmd=1
                        break 
        if cmd:
            continue
        answer+=1
    return answer