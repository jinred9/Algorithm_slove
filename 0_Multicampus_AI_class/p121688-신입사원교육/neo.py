from itertools import combinations


def solution(ability, number):
    n = len(ability)
    minimum = float('INF')

    def dfs(x, arr):
        nonlocal minimum

        if x == number:
            total = sum(arr)
            if total < minimum:
                minimum = total
            return

        for case in combinations(range(n), 2):
            copy_arr = arr[:]
            p1, p2 = case
            copy_arr[p1] = copy_arr[p2] = copy_arr[p1] + copy_arr[p2]

            if sum(copy_arr) > minimum:
                continue

            dfs(x+1, copy_arr)

    dfs(0, ability)

    return minimum


print(solution([10, 3, 7, 2], 2))
print(solution([1, 2, 3, 4], 3))
