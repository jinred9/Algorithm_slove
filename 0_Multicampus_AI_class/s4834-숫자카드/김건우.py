
import sys

sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = int(input())

for test_case in range(1, T + 1):

    N = int(input())  # 카드 장수

    # 카드 종류 : 실제 코드에서 쓰지 않고, 대신 card_count의 index를 활용한다.
    # card =     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 각 번호 별 카드 갯수
    card_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # N개의 숫자 (49679)
    card_num_list = list(map(int, input()))
    # 소트 (46799)
    card_num_list.sort()

    # unique_card (4679)
    unique_card = set(card_num_list)

    # 1. 각 카드가 몇 장인지 센다.
    for i in range(len(unique_card)):
        j = 0
        # unique_card 와 소트된 카드 리스트를 비교하여
        # 카드가 발견되면 카드 갯수(card_count)에 1을 추가한다.
        while j < N:
            if unique_card[i] == card_num_list[j]:
                card_count[i] += 1
                j += 1
            else:
                break


        #                	[ 4 9 6 7 9 ]
        # 가장 많은 카드 장수	[ 1 1 1 1 2 ]
        max_card_count = max(card_count)

        # [ 0 8 2 7 1 ]
        # [ 1 1 1 1 1 ]

        # 2. 가장 많은 카드 장수에 해당하는 숫자들
        max_cards = []
        for i in range(10):
            #  가장 많은 카드 갯수(1) ==  카드 갯수(1)
            if max_card_count == card_count[i]:
                # index를 카드번호로 저장
                max_cards.append(i)

        # 3. 가장 많은 카드 중에 숫자가 가장 큰 것
        max_card = max(max_cards)
        # T(테스트 케이스 번호),  가장 많은 카드의 숫자,  가장 많은 카드의 장 수
        print(f'#{test_case} {max_card} {max_card_count}')


# # 서유빈님 코드
# from collections import Counter # Counter 가져오기
#
# import sys
# sys.stdin = open('input.txt') # 'input.txt' 파일 open
#
# T = int(input()) # 'input.txt'에서 test_case 갯수를 input으로 받음
#
# for test_case in range(1, T+1): # test_case 갯수 만큼 for문 돌림
#     N = int(input())
#
#     numbers_list = list(map(int, str(input()))) # 각 숫자 리스트 엘리먼트로 리스트 형성
#     numbers_list.sort(reverse=True) # 내림차순으로 리스트 변경, 큰 값을 제일 앞에 가져오기
#
#     cnt = Counter(numbers_list) # Counter class 가져오고, numbers_list 빈도수를 값으로 가지고 있는 딕셔너리로 변환
#     print(cnt)
#
#     # most_common(n)함수는 n개의 최빈값 리턴; cnt의 최빈값을 리스트에 담긴 튜플 형태로 리턴
#     the_mode = cnt.most_common(1)[0][0] # 튜플 안 첫번째 값은 the_mode 숫자 (가장 많은 카드에 적힌 숫자)
#     how_many_numbercards = cnt.most_common(1)[0][1] # 튜플 안 두번째 값은 how_many_numbercards 변수 값 (그 카드가 몇 장인지)
#
#     print(f'#{test_case} {the_mode} {how_many_numbercards}') # 최빈값과 최빈값카드가 몇장있는지 출력