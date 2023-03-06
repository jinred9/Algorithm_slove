def solution(numbers, target):
    count = 0   # target을 만들 수 있는 횟수를 0으로 초기화한다

# 덧셈을 해주는 DFS함수
    def dfs(sum_now, index):
        nonlocal count
        if index == len(numbers):   # index가 더할 숫자들의 갯수와 같은 경우
            if sum_now == target:   # 현재 합이 target과 같다면
                count += 1   # count 수를 1개 늘려주고
            return   # 반환한다
# +, - 두개의 분기가 있는 DFS이므로 재귀의 횟수는 2번 진행한다
        dfs(sum_now + numbers[index], index + 1)
        dfs(sum_now - numbers[index], index + 1)

    dfs(0, 0)
    return count


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
