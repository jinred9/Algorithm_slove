# ==========================================================
# 최적화 필요
# ==========================================================

import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    card_num = int(input())
    card = list(map(int, str(input())))
    card_only = list(set(card))
    count = 0
    count_max = 0
    card_dict = {}
    max_card = 0
    for card_one in card_only:
        count = 0
        for card_select in card:
            if card_one == card_select:
                count += 1
        card_dict[card_one] = count
    max_value = max(card_dict.values())
    for k, v in card_dict.items():
        if v == max_value and max_card < k:
            max_card = k
            count_max = v
    print("#{} {} {}".format(test_case, max_card, count_max))
