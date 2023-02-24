#1. git pull
#2. 자기 브랜치에서 자기 이름으로 파일 만들기
#3. 문제 풀기
#4. 푼 코드 add -> commit
#5.git push orgin <브랜치이름>
def solution(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i

    return sum


