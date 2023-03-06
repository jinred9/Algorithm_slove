# 1. git pull
# 2. 자기 브랜치에서 자기 이름으로 파일 만들기
# 3. 문제 풀기
# 4. 푼 코드 add , commit 하기

def solution(n):
    total = 0
    # 1부터 n까지
    for i in range(1, n + 1):
        if n % i == 0:
            total +=i

    return total

