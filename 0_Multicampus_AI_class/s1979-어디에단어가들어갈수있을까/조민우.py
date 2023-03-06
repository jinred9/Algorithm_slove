import sys
sys.stdin = open("input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
   N, K = map(int, input().split())
   # N * N 행렬
   puzzle = [list(map(int, input().split())) for i in range(N)]
   word1 = 0

   # row 찾기

   for i in range(N):
      # 1이 연속되는 횟수
      # zip 사용해서 전치행렬만들기
      puzzle_col = (list(zip(*puzzle)))
      continuous = 0
      col_continuous = 0
      for j in range(N):
         if puzzle[i][j] == 1:
            continuous += 1
            if j == N - 1:
               if continuous == K:
                  word1 += 1
         elif puzzle[i][j] == 0:
               if continuous == K:
                  word1 += 1
               continuous = 0

         # col 찾기
         if puzzle_col[i][j] == 1:
            col_continuous += 1
            if j == N - 1:
               if col_continuous == K:
                  word1 += 1
         elif puzzle_col[i][j] == 0:
            if col_continuous == K:
               word1 += 1
            col_continuous = 0




   print(f't#{test_case} {word1}')

# import sys
# sys.stdin = open("input.txt", "r")
# T = int(input())
#
# for test_case in range(1, T + 1):
#    N, K = map(int, input().split())
#    puzzle = [list(map(int, input().split())) for _ in range(N)]
#    word = 0
#    # row 기준
#    for i in range(N):
#       cnt_row = 0
#       for j in range(N):
#          if puzzle[i][j] == 0:
#             if cnt_row == K:
#                word += 1
#             cnt_row = 0
#          else:
#             cnt_row += 1
#       if cnt_row == K:
#          word += 1
#
#    # col 기준
#    for j in range(N):
#       cnt_col = 0
#       for i in range(N):
#          if puzzle[i][j] == 0:
#             if cnt_col == K:
#                word += 1
#             cnt_col = 0
#          else:
#             cnt_col += 1
#       if cnt_col == K:
#          word += 1
#
#    print(f"#{test_case} {word}")










