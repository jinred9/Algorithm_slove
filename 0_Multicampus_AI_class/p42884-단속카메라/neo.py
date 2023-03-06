def solution(routes):
    routes.sort(key=lambda x: x[1])
    # 일단 첫 차의 맨 마지막에 greedy 하게 카메라 설치
    last_camera = routes[0][1]
    # 설치 += 1
    answer = 1

    for idx in range(1, len(routes)):
        start, end = routes[idx]
        # 현재 차량의 진입이 마지막 카메라 보다 늦다면 (카메라에 안걸린다면)
        if start > last_camera:
            last_camera = end
            answer += 1

        # # 차가 카메라에 걸린다면,
        # if start <= last_camera <= end:
        #     continue
        # # 차가 카메라에 안걸리면?
        # else:
        #     # 해당 차의 맨 마지막에 greedy하게 카메라 설치
        #     last_camera = end
        #     # 설치 += 1
        #     answer += 1

    return answer




# 2
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))