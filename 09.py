def solution(decimal):
    stack = []
    while decimal > 0:
        a = decimal % 2
        stack.append(str(a))
        decimal //= 2
    result = ' '
    while stack:
        result += stack.pop()
    print(result)
    
decimal = 10
#decimal = 27
#decimal = 12345
solution(decimal)

        