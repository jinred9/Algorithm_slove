import sys

sys.stdin = open("input.txt", "r")

T = int(input())    # 테스트 케이스

for test_case in range(T):
    card_num = int(input())
    card_list = input()
    card_info = {}

    for c in card_list:
        if card_info.get(c):
            card_info[c] += 1
        else:
            card_info[c] = 1

    sorted_key = sorted(card_info)
    Max = 0
    answer_key = '1'
    for key in sorted_key:
        if card_info[key] >=Max:
            Max = card_info[key]
            answer_key = key


    print(f'#{test_case} {answer_key} {Max}')

