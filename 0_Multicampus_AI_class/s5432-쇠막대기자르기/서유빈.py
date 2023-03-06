import sys
sys.stdin = open('input.txt') # 'input.txt' 파일 open

T = int(input()) # 'input.txt'에서 test_case 갯수를 input으로 받음
for test_case in range(1, T+1): # test_case 갯수 만큼 for문 돌림
    iron_rod_list = list(input()) # 'input.txt'에서 괄호 샘플 받고 리스트로 바꿈

    # 변수 초기화 및 할당
    rod = 0 # 쇠 막대 갯수
    counted_rod = 0 # 최종 쇠 막대 갯수 (잘린 막대 포함)
    number_of_brackets = len(iron_rod_list) # 리스트 내부 샘플 괄호의 갯수
    bracket_item = 0 # 샘플 괄호 리스트 번호(순서)

    while bracket_item < number_of_brackets: # 리스트 끝에 도달할 때까지 while문
        if iron_rod_list[bracket_item] == '(' and iron_rod_list[bracket_item+1] == ')': # 레이저 인식
            counted_rod += rod # 쌓인 막대만큼 최종 막대 갯수 추가 (겹친 것 계산)
            bracket_item += 2 # 레이저 인식했으니 그 다음 괄호 스킵

        elif iron_rod_list[bracket_item] == '(': # '(' 왼쪽 끝만 있을 경우
            rod += 1 # 막대 갯수 추가
            bracket_item += 1 # 그 다음 괄호로 이동

        else: # ')' 오른쪽 끝만 있을 경우
            counted_rod += 1 # 최종 막대 갯수 추가
            rod -= 1 # 막대 갯수 감소
            bracket_item += 1 # 그 다음 괄호로 이동

    print('#{} {}'.format(test_case, counted_rod)) # 최종 결과 출력