import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    string_phrase = input()
    string_list = []
    # for문으로 리스트에 담겼던 문자와 담으려고 하는 문자가 같을 때, pop으로 제거
    for string in string_phrase:
        if string_list and string == string_list[-1]:
            string_list.pop()
        else:
            string_list.append(string)

    print('#{}'.format(test_case), len(string_list))
