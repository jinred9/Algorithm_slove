def solution(command):
    answer = [0, 0]
    dire = [
        0[0, 1],
        1[1, 0],
        2[0, -1],
        3[-1, 0]
    ]
    state = 0
    for order in command:
        state %= 4
        if order == 'G':
            answer[0] += dire[state][0]
            answer[1] += dire[state][1]
            # answer = [x+y for x, y in zip(answer, dire[state])]
        if order == 'R':
            state += 1
        if order == 'L':
            state -= 1
        if order == 'B':
            answer[0] -= dire[state][0]
            answer[1] -= dire[state][1]
            # answer = [x-y for x, y in zip(answer, dire[state])]
    return answer


print(solution("GRGRGRB"))