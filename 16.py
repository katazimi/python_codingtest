from collections import deque

def solution(progresses, speeds):
    queue = deque(progresses)
    speed_queue = deque(speeds)
    run = False
    result_item = 0
    result = []

    while len(queue) > 0:
        for i in range(len(queue)):
            queue.append(queue.popleft() + speed_queue[0])
            speed_queue.append(speed_queue.popleft())
        
        if queue[0] >= 100:
            while queue and queue[0] >= 100:
                queue.popleft()
                result_item += 1
        
        if result_item > 0:
            result.append(result_item)
            result_item = 0
    print(result)
        
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
solution(progresses, speeds)