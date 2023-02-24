import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = [2,3,5,7,11]
    cnt = [0,0,0,0,0]
    for i in range(len(num)):
        while True: # '0' 즉 값이 False가 될 때 까지 무한루프 돌리기
            if N % num[i] == 0: # i로 소인수분해 되는 경우라면
                N = N // num[i] # i로 나누어 N에 몫을 남기어 준다.
                cnt[i] += 1 # i cnt에 +1 증가
            else:
                break
    print(f'#{tc} {cnt}')