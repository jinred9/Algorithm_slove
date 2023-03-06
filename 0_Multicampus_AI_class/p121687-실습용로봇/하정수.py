def solution(command):
    heading = 1
    location = [0, 0]
    for order in command:
        if order == 'R':
            heading += 1
            heading = heading % 4
        if order == 'L':
            heading -= 1
            heading = heading % 4
        if order == 'G':
            if heading == 1:
                location[1] = location[1] + 1
            if heading == 2:
                location[0] = location[0] + 1
            if heading == 3:
                location[1] = location[1] - 1
            if heading == 0:
                location[0] = location[0] - 1
        if order == 'B':
            if heading == 1:
                location[1] = location[1] - 1
            if heading == 2:
                location[0] = location[0] - 1
            if heading == 3:
                location[1] = location[1] + 1
            if heading == 0:
                location[0] = location[0] + 1
    answer = location
    return answer


# def solution(command):
#     heading = 1
#     location = [0, 0]
#     headings = [[-1, 0], [0, 1], [1, 0], [0, -1]]
#     for order in command:
#         if order == 'R':
#             heading += 1
#             heading = heading % 4
#         if order == 'L':
#             heading -= 1
#             heading = heading % 4
#         if order == 'G':
#             location = [x + y for x, y in zip(location,headings[heading])]
#
#         if order == 'B':
#             location = [x - y for x, y in zip(location,headings[heading])]
#
#     answer = location
#     return answer


print(solution("GRGLGRG"))
print(solution("GRGRGRB"))
