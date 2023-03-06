import sys
sys.stdin = open('input.txt')

for i in range(10):
	tc = i + 1
	length = int(input())
	tall = list(map(int, input().split()))
	count = 0
	for s in range(length):
		if s in [0,1,length - 1, length - 2]:
			continue
		elif tall[s] <= tall[s+1] or tall[s] <= tall[s+2] or tall[s] <= tall[s-1] or tall[s] <= tall[s-2]:
			continue
		else:
			count += tall[s] - max(tall[s+1], tall[s-1], tall[s+2], tall[s-2])

	print(f'#{tc} {count}')



