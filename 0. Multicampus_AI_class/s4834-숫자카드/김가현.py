import sys

sys.stdin = open("input.txt", "r")

T = int(input())    # 테스트 케이스
for test_case in range(1, T+1):
    card = int(input())    # 카드 장수
    num = list(map(int, str(input())))    # 카드 숫자별 리스트로 변환

    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 카드 숫자별 장수 초기값
    for i in range(0, card):    # 카드 숫자별 장수 카운트
        count[num[i]] += 1

    num_max = max(count)
    index = count.index(num_max)

    for i in range(0, 10):  # max 값 중 큰 숫자 구하기
        if count[i] >= num_max:
            index = i

    print(f"#{test_case} {index} {num_max}")