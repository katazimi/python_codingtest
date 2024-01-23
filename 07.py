def solution(dirs):
    x, y = 0, 0 # 좌표
    count = 0 # 방문 횟수
    dirs_lst = list(dirs) # dirs의 문자열을 분리하여 리스트에 저장
    dirs_len = len(dirs_lst) # dirs의 길이 
    route = [] # 중복을 찾기위해 x,y의 좌표값과 dirs의 값을 저장하는 리스트
    dup = 0 # 중복된 횟수
    expt = 0 # 중복과 x와 y값이 벗어난 경우가 같은경우 이 값을 더해 해결
    for i in range(dirs_len):
        if dirs_lst[i] == 'U':
            if y < 5:
                y = y + 1
                count = count + 1
            else:
                if expt == 0:
                    expt = 1
                expt += 1
        elif dirs_lst[i] == 'D':
            if y > -5:
                y = y - 1
                count = count + 1
            else:
                if expt == 0:
                    expt = 1
                expt += 1
        elif dirs_lst[i] == 'L':
            if x > -5:
                x = x - 1
                count = count + 1
            else:
                if expt == 0:
                    expt = 1
                expt += 1
        elif dirs_lst[i] == 'R':
            if x < 5:
                x = x + 1
                count = count + 1
            else:
                if expt == 0:
                    expt = 1
                expt += 1
        route.append([x,y,dirs_lst[i]])
    for i in range(len(route)):
        for j in range(i+1, len(route)):
            if route[i][0] == route[j][0] and route[i][1] == route[j][1] and route[i][2] == route[j][2]:
                dup += 1
    if expt == 2:
        expt = 1
    count = count - dup + expt
    print(count)

#dirs = "ULURRDLLU"
dirs = "LULLLLLLU"
solution(dirs)

        
