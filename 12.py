def solution(prices):
    stack = []
    result = []
    count = 0
    for i in prices:
        stack.append(i)
    for j in range(len(stack)):
        count = 0
        for k in range(j+1, len(stack)):
            if stack[k] >= stack[j]:
                count += 1
        result.append(count)
    print(result)

prices = [1,2,3,2,3]
solution(prices)