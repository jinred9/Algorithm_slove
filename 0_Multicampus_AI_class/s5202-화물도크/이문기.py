import sys
sys.stdin = open('input.txt', 'r')

for tc in range(int(input())):
	result = 0
	car_list = list()
	ok_list = list()
	for i in range(int(input())):
		car_list.append(list(map(int, input().split())))
	car_list.sort(key=lambda x: x[1])
	for i in range(len(car_list)):
		if i == 0:
			ok_list.append(car_list[i])
			result += 1
		elif car_list[i][0] >= ok_list[-1][1]:
			ok_list.append(car_list[i])
			result += 1
		elif car_list[i][0] < car_list[i-1][1]:
			continue
	print(f'#{tc+1} {result}')

################################

for tc in range(int(input())):
	result = 1
	car_list = list()
	for i in range(int(input())):
		car_list.append(list(map(int, input().split())))
	car_list.sort(key=lambda x: x[1])
	end_time = car_list[0][1]
	for i in range(1, len(car_list)):
		start = car_list[i][0]
		end = car_list[i][1]
		if start >= end_time:
			end_time = end
			result += 1
		else:
			continue
	print(f'#{tc+1} {result}')






