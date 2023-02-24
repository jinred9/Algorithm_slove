def solution(routes):
    answer = 0

    routes.sort(key=lambda route:route[1])

    print(routes)

    while len(routes)!=0:
        idx = 0
        last_cam = routes[0][1]
        for i in range(len(routes)):
            if routes[idx][0] <= last_cam:
                routes.pop(idx)
            else:
                idx += 1
        answer += 1
    return answer
