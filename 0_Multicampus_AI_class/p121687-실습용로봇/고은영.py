
def solution(command):
    loc = [0, 0]
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    chk = 0

    for i in command:
        chk %= len(direction)
        if i =="G" :
            loc[0] += direction[chk][0]
            loc[1] += direction[chk][1]
        elif i == "L":
            chk -= 1
        elif i == 'R':
            chk += 1
        elif i == "B":
            loc[0] -= direction[chk][0]
            loc[1] -= direction[chk][1]

    return loc

print(solution("GRGRGRB"))
