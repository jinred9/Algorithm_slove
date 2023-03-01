# 1.git pull
# 2. 자기 브랜치에서 자기 이름으로 만들기
# 3. 문제풀기
# 4. 푼 코드 add => commit
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer