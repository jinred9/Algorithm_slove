from itertools import permutations
def solution(k, dungeons):
    answer = -1
    N = len(dungeons)
    for plan in permutations(dungeons, N):
        count = 0
        hp = k
        for require, damage in plan:
            if hp < require or hp <= 0:
                break
            else:
                hp -= damage
                count += 1
        if count > answer:
            answer = count
        if answer == N:
            return answer




    return answer



solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])
print(solution(80, [[80, 20], [50, 40], [30, 10]]))