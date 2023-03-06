def solution(command):
    Translate = ['G','R','L','B']

    Now_dir = [[0,1],[1,0],[0,-1],[-1,0]]
    flag = 0
    now_loc = [0,0]
    for c in command:
        if c == 'G':
            now_loc[0] = now_loc[0] + Now_dir[flag][0]
            now_loc[1] = now_loc[1] + Now_dir[flag][1]
        elif c == 'R':
            flag+=1
            if flag > 3:
                flag = 0
        elif c == 'L':
            flag-=1
            if flag<0:
                flag = len(Now_dir)-1
        else:
            now_loc[0] = now_loc[0] - Now_dir[flag][0]
            now_loc[1] = now_loc[1] - Now_dir[flag][1]


    return now_loc











print(solution('GRGLGRG'))
print(solution( "GRGRGRB" ))