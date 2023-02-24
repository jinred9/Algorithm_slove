from itertools import permutations

def solution(k, dungeons):
    answer = -1
    k = k
    result = []
    dungeons = dungeons
    count_maximum = []
    p = list(permutations(dungeons, 3))
    for i in p:
        count = 0
        pirodo = k
        print(i)
        for j in i:
            if j[0] <= pirodo and j[1] <= pirodo:
                pirodo -= j[1]
                count += 1
                count_maximum.append(count)
                print(count_maximum)

    print(count_maximum)
    return answer

print(solution(80, [[80, 20], [50, 40], [30, 10]]))