def solution(numbers, target):
    result = [0]   # 맨 처음값은 0으로 초기화한다 (함수를 리스트로 받으므로 리스트로 초기화)
    for number in numbers:   # 정수들의 수만큼
        result = nxt(result, [number, -number])   # 더하기, 빼기 한 결과를 반복한다
    return result.count(target)   # 최종 값에서 원하는 값의 개수를 반환한다


# 들어온 숫자들을 이전 숫자들에 각각 더해주는 함수
def nxt(now, to_add):   # 현재 담겨져 있는 리스트와 더해줄 숫자를 입력받는다
    result = []   # 계산 결과를 담을 리스트
    for i in range(len(now)):   # 현재 리스트의 수 만큼
        for j in range(len(to_add)):   # 더해줄 숫자를 각각
            result.append(now[i] + to_add[j])   # 더해서 결과에 담아준 것을
    return result   # 반환한다


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
