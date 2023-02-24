import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for test_case in range(1, T + 1):
    sentence = input()   # 문자열을 저장
    checks = [0]   # 확인할 리스트에 0을 입력(숫자값)
    last = 0   # 마지막 위치를 0으로 초기화
    for alph in sentence:   # 알파벳 갯수만큼 반복
        if alph == checks[last]:   # 현재 알파벳이 마지막과 같다면
            checks.pop()   # 저장된 마지막값을 pop하고
            last -= 1   # 마지막 위치를 1 줄여준다
        else:
            checks.append(alph)   # 현재 알파벳을 리스트에 추가하고
            last += 1   # 마지막 위치를 1 늘려준다
    print(f'#{test_case} {len(checks) - 1}')   # 반환할 때 처음에 추가한 0이 있으므로 길이를 1개 줄여준다
