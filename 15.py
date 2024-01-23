from collections import deque

def solution(N, k):
    queue = deque(range(1, N+1))

    while len(queue) > 1:
        for i in range(k-1):
            queue.append(queue.popleft())
        queue.popleft()
    print(queue[0])

N = 5
k = 2
solution(N, k)