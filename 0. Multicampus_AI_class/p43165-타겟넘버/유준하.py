def solution(numbers, target):
    signs = [1, -1]   # - 혹은 +를 부여하기 위해 signs 리스트 생성
    count = 0    # 조건을 충족하는 것이 몇개 있는지 확인 할 수 있는 count 변수

    def dfs(n, result, sign):   # 부분집합의 합 참조
        global count
        if n == len(numbers):   # n이 증가하면서 numbers에 있는 모든 숫자에 대해 연산 했을 경우
            if result == target:  # 조건 확인 성립 시 count += 1 하고 리텅
                count += 1
            return

        result += numbers[n] * sign  # 연산 결과 저장 시 numbers의 값의 부호 바뀌는 것 반영해서 연산
        dfs(n+1, result, 1)  # 양수, 음수에 대한 연산 재귀
        dfs(n+1, result, -1)

    for sign in signs:
        dfs(0, 0, sign)

    return count//2  # 양수 음수 나눠서 연산 하면서 2번 중복되기 때문에 2를 나눠준다

    solution([1, 1, 1, 1, 1], 3)