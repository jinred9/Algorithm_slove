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




from collections import Counter
import sys
sys.stdin = open('input.txt') # 'input.txt' 파일 open

T = int(input()) # 'input.txt'에서 test_case 갯수를 input으로 받음

for test_case in range(1, T+1): # test_case 갯수 만큼 for문 돌림
    N = int(input())

    numbers_list = list(map(int, str(input()))) # 각 숫자 리스트 엘리먼트로 리스트 형성
    numbers_list.sort(reverse=True) # 내림차순으로 리스트 변경, 큰 값을 제일 앞에 가져오기

    cnt = Counter(numbers_list) # Counter class 가져오고, numbers_list 빈도수를 값으로 가지고 있는 딕셔너리로 변환

    # most_common(n)함수는 n개의 최빈값 리턴; cnt의 최빈값을 리스트에 담긴 튜플 형태로 리턴
    the_mode = cnt.most_common(1)[0][0] # 튜플 안 첫번째 값은 the_mode 숫자 (가장 많은 카드에 적힌 숫자)
    how_many_numbercards = cnt.most_common(1)[0][1] # 튜플 안 두번째 값은 how_many_numbercards 변수 값 (그 카드가 몇 장인지)

    print(f'#{test_case} {the_mode} {how_many_numbercards}') # 최빈값과 최빈값카드가 몇장있는지 출력

    import sys

    sys.stdin = open('input.txt')

    # 테스트 케이스 개수
    T = int(input())

    for test_case in range(1, T + 1):

        N = int(input())  # 카드 장수

        # 카드 종류
        card = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 카드 개수 초기화
        card_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        card_num = input()  # N개의 숫자

        # 카드 소트
        card_num_list = list(map(int, card_num))
        card_num_list.sort()

        # unique_card
        unique_card = set(card_num_list)

        # 각 카드가 몇 장인지 센다.
        for i in unique_card:
            for num in card_num_list:
                # unique_card 와 소트된 카드 리스트릴 비교하여
                # 카드가 발견되면 카드 갯수(card_count)에 1을 추가한다.
                if i == num:
                    card_count[i] += 1

        # 가장 많은 카드 장수
        max_card_count = max(card_count)

        # 가장 많은 카드
        max_cards = []
        for i in range(10):
            if max_card_count == card_count[i]:
                max_cards.append(i)

        # 가장 많은 카드 중에 숫자가 가장 큰 것
        max_card = max(max_cards)

        print(f'#{test_case} {max_card} {max_card_count}')