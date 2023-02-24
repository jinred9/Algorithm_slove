# n : 상자 개수
import sys

sys.stdin = open("input.txt", "r")

T = int(input())    # test case 입력

for test_case in range(1, T+1):
    N, Q = map(int, input().split())    # N : 상자개수, Q : 작업수행횟수

    box = [0 for i in range(N)]     # 상자개수만큼 0으로 초기화

    for i in range(1, Q+1):
        L, R = map(int, input().split())   # 작업수행횟수만큼 작업구간 입력받기
        for j in range(L-1, R):
            box[j] = i   # 작업구간만큼 숫자 변경

    print(f"#{test_case}", end=' ')
    print(*box)     # * : 리스트(대괄호) 값만 가져오기



