# 1. git pull
# 2. 자기 브랜치에서 자기 이름으로 파일 만들기
# 3. 문제 풀기
# 4. 푼 코드 add => commit

int solution(int n)
{
    int answer = 0;

    for(int i = 1; i <= n; i++)
        if(n % i == 0)
            answer += i;

    return answer;
}