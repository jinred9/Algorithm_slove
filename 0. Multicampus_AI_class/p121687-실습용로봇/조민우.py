
def solution(command):
    head = 0
    x = 0
    y = 0
    for direction in command:
        if direction == 'R':
            head = (head + 1) % 4
        elif direction == 'L':
            head = (head - 1) % 4
        elif direction == 'G':
            if head == 0:
                y += 1
            elif head == 1:
                x += 1
            elif head == 2:
                y -= 1
            else:
                x -= 1
        else:
            if head == 0:
                y -= 1
            elif head == 1:
                x -= 1
            elif head == 2:
                y += 1
            else:
                x += 1

    answer = [x, y]
    return answer

print(solution("GRGLGRG"))
print(solution("GRGRGRB"))

# 연산 시간 초과 코드 수정중 원본 잊음
    # for direction in command:
    #     if direction == 'R':
    #         head = (head + 1) % 4
    #     if direction == 'L':
    #         head = (head - 1) % 4
    #     elif direction == 'G':
    #         if head == 0:
    #             y += 1
    #         elif head == 1:
    #             x += 1
    #         elif head == 2:
    #             if direction == 'G':
    #                 y -= 1
    #         else:
    #             if direction == 'G':
    #                 x -= 1
    #     else:
    #         if head == 0:
    #             y -= 1
    #         elif head == 1:
    #             x -= 1
    #         elif head == 2:
    #             y += 1
    #         else:
    #             x += 1
