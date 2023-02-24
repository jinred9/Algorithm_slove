def solution(command):
    answer = []
    type = ['R', 'L', 'G', 'B']
    x, y = 0, 0
    status = 0
    for position in command:
        if position == type[0]:
            status = (status + 1) % 4
        elif position == type[1]:
            status = (status - 1) % 4
        elif position == type[2]:
            if status == 0:
                y += 1
            elif status == 1:
                x += 1
            elif status == 2:
                y -= 1
            else:
                x -= 1
        else:
            if status == 0:
                y -= 1
            elif status == 1:
                x -= 1
            elif status == 2:
                y += 1
            else:
                x += 1
    answer.append(x)
    answer.append(y)
    return answer



print(solution("GRGLGRG"))
print(solution("GRGRGRB"))