def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        print(True)
    else:
        print(False)

s = "(())()"
#s = "((())()"
solution(s)
