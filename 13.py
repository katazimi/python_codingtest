def solution(board, moves):
    stack = []
    columm = len(board) -1 
    row = len(board[0])
    catch = []
    overlap = False
    result = 0

    for i in range(row):
        stack.append([])

    for i in range(columm, -1, -1):
        for j in range(row):
            if board[i][j] != 0:
                stack[j].append(board[i][j])

    for i in moves:
        if len(stack[i-1]) > 0:
            catch.append(stack[i-1].pop())
    
    while overlap == False:
        run = 0
        for i in range(0, len(catch) - 3):
            if catch[i] == catch[i+1]:
                catch.pop(i)
                catch.pop(i)
                result += 2
                run = 1
        if run == 0:
            overlap = True

    print(catch) 
    print(result)              
    
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board,moves)

