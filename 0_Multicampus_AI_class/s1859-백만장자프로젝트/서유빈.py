import sys
sys.stdin = open('input.txt')
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     answer = sum(numbers)
#     print(f'#{test_case} {answer}')


# 3
# 3
# 10 7 6 <- arr
# 3
# 3 5 9 <- arr
# 5
# 1 1 3 1 2 <- arr

test_case = int(input())  # 전체 test_case 갯수
for i in range(test_case):  # test_case마다
    num = int(input())
    answer = 0  # 정답
    arr = list(map(int, input().split()))  # 배열 입력 받기
    sell_price = 0  # 현재 판매 가격(maximum 가격)

    for value in arr[::-1]:  # 배열 거꾸로 순회 (미래)
        if value >= sell_price:  # 현재 값이 최댓값보다 크거나 같다면
            sell_price = value  # max price 업데이트
        else:
            answer += sell_price - value  # 아니면 정답값에 가격차이를 더함
    print("#", i + 1, " ", answer, sep="")  # 출력 양식에 맞춰서 출력
