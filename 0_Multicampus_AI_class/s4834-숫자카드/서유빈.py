from collections import Counter # Counter 가져오기

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