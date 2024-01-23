def solution(n, k, cmd):
    stack = []
    past = []
    for i in range(n):
        stack.append("O")
    
    for i in range(len(cmd)):
        cmd_list = cmd[i].split()
        if cmd_list[0] == "U":
            k = k - int(cmd_list[1])
            if k < 0:
                k = 0
        elif cmd_list[0] == "D":
            k = k + int(cmd_list[1])
            if k > n:
                k = n
        elif cmd_list[0] == "C":
            stack[k] = "X"
            past.append(k)
        elif cmd_list[0] == "Z":
            stack[past.pop()] = "O"
    print(stack)

n = 8
k = 2
#cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
solution(n, k, cmd)