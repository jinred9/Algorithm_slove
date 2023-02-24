# 1. git pull
# 2. 자기 브랜치에서 자기 이름 으로 파일 만들기
# 3. 문제 풀기
# 4. 푼 코드 add => commit
# 5. git push origin <브랜치이름>
def solution(n):
    answer = 0
    # 1 ~ n 까지 모두 순회하며
    for x in range(1, n + 1):
        # n이 x로 나누어 떨어지면 => 나눈 나머지가 0이라면,
        if n % x == 0:
            # 약수니까 answer 에 더한다.
            answer += x

    return answer