# 수직 선상에서 겹치는 부분을 찾는다
# routes[0][1] [0][0] 사이의 값들은 찾는다
# 찾았을 시 그 지점으로 위치를 갱신해 준다.
# 카메라의 위치는 겹치는 출입 지점이 최소지점이다.

def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1])
    cameraList = [routes[0][1]]
    for k in range(1, len(routes)):
        if routes[k][0]<=cameraList[-1] and routes[k][1]>=cameraList[-1]:
            continue
        else:
            cameraList.append(routes[k][1])
    return len(cameraList)

def solution(routes):
    check = 30001

print(solution([[-20,-15], [-14,-5], [-18,-13], [-19,-3]]))

