def solution(command):
    answer = []
    x = 0
    y = 0
    z = 1
    for _ in command:
        if _ == 'R':
            z += 1
        elif _ == 'L':
            z -= 1
        elif _ == 'G':
            if z % 4 == 1:
                y += 1
            if z % 4 == 2:
                x += 1
            if z % 4 == 3:
                y -= 1
            if z % 4 == 0:
                x -= 1
        elif _ == 'B':
            if z % 4 == 1:
                y -= 1
            if z % 4 == 2:
                x -= 1
            if z % 4 == 3:
                y += 1
            if z % 4 == 0:
                x += 1
    answer = [x, y]
    return answer



# print(solution("GR"))
# solution("GRGLGRG")
print(solution("GRGLGRG"))
# # [2, 2]
print(solution("GRGRGRB"))
# # [2, 0]
