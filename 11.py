def solution(s):
    first_pop = ""
    second_pop = ""
    w = []
    stack = []
    for i in s:
        stack.append(i)
    for j in range(len(stack)//2):
        for k in range(len(stack)-1):
            if stack[k] == stack[k+1]:
                w = []
                w.append(k)
        if len(w) > 0:
            stack.pop(w[0])
            stack.pop(w[0])
    if len(stack) > 1:
        print(0)
    elif len(stack) == 0:
        print(1)
    
s = 'cdcd'
solution(s)