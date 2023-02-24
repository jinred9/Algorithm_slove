문제 설명
n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.
입출력 예
numbers	target	return
[1, 1, 1, 1, 1]	3	5
[4, 1, 2, 1]	4	2
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.

입출력 예 #2

+4+1-2+1 = 4
+4-1+2-1 = 4
총 2가지 방법이 있으므로, 2를 return 합니다.
function
solution(numbers, target)
{
    let
answer = 0;

function
dfs(k)
{
if (k === numbers.length)
{
    let
sum = 0;
for (let i = 0; i < numbers.length; i++)
{
    sum += numbers[i]
}

return sum === target ? answer + +: answer;

}
dfs(k + 1);

numbers[k] *= -1;
dfs(k + 1);
}

dfs(0);

return answer;
}
profile
채림

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
