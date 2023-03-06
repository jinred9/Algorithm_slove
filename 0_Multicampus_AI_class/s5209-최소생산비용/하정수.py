import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    product = int(input())   # 제품 수
    matrix = [list(map(int, input().split())) for _ in range(product)]   # 제품의 공장별 생산비용 저장
    minimum = float('inf')   # 최솟값을 무한으로 초기화
    is_done = [False] * product   # 사용한 공장 리스트를 False로 초기화

    def search(idx, total):
        global minimum   # global로 minimum 사용
        if minimum < total:   # 더해가다가 total이 minimum을 넘는 순간
            return   # 더 깊이 계산하지 않아도 된다

        if idx == product:   # 제품 수만큼 진행했을 때
            minimum = total   # total을 minimum에 저장(위에서 minimum이 total보다 크면 반환했기 때문에 항상 작다)
            return

        for nth in range(len(matrix[0])):   # 공장 종류별로
            if not is_done[nth]:   # 사용하지 않은 공장이면
                is_done[nth] = True   # 사용내역을 바꿔주고
                search(idx+1, total + matrix[nth][idx])   # 인덱스(제품 번호)와 생산시간을 넘겨준다
                is_done[nth] = False   # 사용내역을 초기화한다
    search(0, 0)

    print(f'#{test_case} {minimum}')
