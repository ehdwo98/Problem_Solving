from collections import deque

def solution(priorities, location):
    answer = 0
    my_doc = [0 for _ in range(len(priorities))]
    my_doc[location] = 1
    queue = deque(priorities)
    while True:

        if not my_doc or max(my_doc) == 0:
            print('Break!')
            break
        if max(queue) == queue[0]:
            queue.popleft()
            del my_doc[0]
            answer += 1
        else:
            queue.append(queue[0])
            my_doc.append(my_doc[0])
            queue.popleft()
            del my_doc[0]


    return answer