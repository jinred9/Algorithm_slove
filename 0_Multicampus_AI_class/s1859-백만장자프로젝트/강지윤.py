import sys
sys.stdin = open('input.txt')


T = int(input())
# def calculate_benefit(li):
#     max = max(li)
#     benefit = 0
#     for i in range(len(li)-1):
#         benefit += max - li[i]
#
#     return benefit
#



for test_case in range(1,T+1):
    everythings = []
    N = int(input())
    numbers = list(map(int,input().split()))
    Max = 0
    Sum = 0
    for i in range(len(numbers)-1,-1,-1):
        if numbers[i] > Max:
            Max = numbers[i]
        else:
            Sum += Max - numbers[i]

    print(f'#{test_case} {Sum}')














