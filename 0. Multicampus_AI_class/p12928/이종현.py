1. git pull
2. 본인 브랜치에서 본인 이름으로 파일 만들기
3. 문제 풀기
4. 푼 코드 add, commit 하기

def solution(n):
    answer = 0
    a = 0
    while n >= a:
        a = a + 1
        if n % a == 0:
            answer = answer + a
    return answer