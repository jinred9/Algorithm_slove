T = int(input())  입력에서 t를읽습니다
for i in range(T):
    N = int(input())
    cards = list(map(int, input().strip()))  T 범위에대해 정수입력.

    각 카드 번호 빈도를 센다.
    count = [0] * 10
    for card in cards:
        count[card] += 1

     가장 빈번한 카드 번호찾는다.
    most_common_card = max(range(10), key=lambda x: (count[x], x))

     결과 출력
    print(f"#{i+1} {most_common_card} {count[most_common_card]}")

함수는 가장 일반적인 카드 번호의 인덱스를 찾는 데 사용됩니다. 동점이 있는
경우 먼저 개수를 비교한 다음 숫자 자체를 비교하는 람다 함수를 사용하여
더 높은 숫자를 선택합니다
. f-문자열은 테스트 사례 번호로 출력 형식을 지정하는 데 사용됩니다.






