def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    camera = -30001
    print(routes)
    cnt = 0
    for i in range(len(routes)):
        s, e = routes[i]
        if camera < s:
            cnt += 1
            camera = e
    answer = cnt

    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))