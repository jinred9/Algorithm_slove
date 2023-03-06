#1. git pull
#2. 자기 브랜치에서 자기 이름으로 파일 만들기
#3. 문제 풀기
#4. 푼 코드 add => commit
#5. git push origin <브랜치이름> (내이름)햣

def solution(n):
    answer = 0
    for i in range(n):
        i += 1
        if n % i == 0:
            answer += i
    return answer