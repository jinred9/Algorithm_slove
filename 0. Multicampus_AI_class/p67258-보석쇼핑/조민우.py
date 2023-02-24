def solution(gems):
    # 입력 받을 잼을 리스트로 표현
    shelf = [i for i in gems]
    # 입력 받은 잼을 set으로 저장해 중복을 삭제
    gem_set =set(shelf)
    gem_count =len(set(shelf))
    end = len(shelf)
    answer = [1,1]
    start = 0


    # if 문을 통해서 i번쨰  보석과 i+1 이 같은지 판별 같다면 i+1로 갱신
    # 입력 받은 잼의 리스트의 길이를 if문의 조건으로 사용
    # i 의 값을 통해서 입력받은 잼의 리스틀 슬라이싱한다 [1:0]

    # 리스트의 i 부터 끝 까지의 길이가 잼의 set의 길이와 같으면 잼을 한번씩 구매한것과 같은 경우의 수
    # 입력받은 값의 길이를 가지고 for문의 범위를 정함
    while True:
        if gem_count == 1:
            break
        if len(set(shelf[start:]) & gem_set) == gem_count:
            if len(set(shelf[:end]) & gem_set) == gem_count:
                end -= 1
            start += 1
        elif (start +1) == end:
            answer = [end-start, end]
            break
        else:
            answer = [start, end+1]
            break
    return answer

print('1',solution(["DIA", "RUBY", "RUBY","DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print('2',solution(["AA", "AB", "AC", "AA", "AC"]))
print('3',solution(["XYZ", "XYZ", "XYZ"]))
print('4',solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))