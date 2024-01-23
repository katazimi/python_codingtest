def solution(N,stages):
    result = []
    fail = []
    max_Search = []
    total = len(stages)
    for i in range(1,N+1):
        fail.append(stages.count(i) / total)
        max_Search.append(stages.count(i) / total)
        total = total - stages.count(i)
    for j in range(0,N):
        max_index = max_Search.index(max(max_Search))
        result.append(max_index + 1)
        max_Search[max_index] = -1
    print(result)
    
N = 5
stages = [2,1,2,6,2,4,3,3]
solution(N,stages)


    