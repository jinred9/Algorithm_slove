def solution(routes):
    routes.sort(key=lambda x: x[1])
    end = None
    camera_count = 0
    for r in routes:
        if end == None:
            end = r[-1]
            camera_count += 1
            continue

        if r[0] > end:
            camera_count += 1
            end = r[1]

    return camera_count


print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))