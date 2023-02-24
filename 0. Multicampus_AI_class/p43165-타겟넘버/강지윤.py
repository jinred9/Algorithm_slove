
def solution(numbers, target):
    count = 0
    #count : target의 갯수
    #target : 탈출 조건
    def dfs(Sum, index):
        nonlocal count
        nonlocal target
        #인덱스를 증가시키면서 더해나간다
        #시작은 0으로 시작
        if index == len(numbers):
            if Sum == target:
                count += 1
            return

        dfs(Sum+numbers[index], index+1)
        dfs(Sum-numbers[index],index+1)

    dfs(0, 0)
    return count



print(solution([1,1,1,1,1],3))
print(solution([4,1,2,1],4))