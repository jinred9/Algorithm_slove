def solution(routes):
	car_list = routes[:]
	answer = 0
	while True:

		x = []
		for i in range(-30000,30001):
			for j in car_list:
				if i in range(j[0],j[1]+1):
					x.append(i)
		max_count = 0
		max_load = 0
		for i in x:
			if i == x[0]:
				max_count = x.count(x[0])
				max_load = i
			elif x.count(i) > max_count:
				max_count = x.count(i)
				max_load = i
		if max_count in [0,1]:
			answer += len(car_list)
			break

		for i in car_list:
			if max_load >= i[0] and max_load <= i[1]:
				car_list = [xy for xy in car_list if xy != i]
		answer += 1
	return answer

y = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(y))