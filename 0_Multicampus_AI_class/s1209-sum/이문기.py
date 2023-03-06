import sys
sys.stdin = open('input.txt')
for gc in range(10):
	tc = gc + 1
	tc_num = int(input())
	array = []
	diag_list = []
	diag_list2 = []
	sum_list = []
	reverse_array = []
	divide_colum_list = []
	for i in range(100):
		array.append(list(map(int, (input().split(" ")))))
	reverse_array = array[::-1]
	array_2 = list(map(list, zip(*array)))
	for i in range(100):
		sum_list.append(sum(array[i]))
		sum_list.append(sum(array_2[i]))
		for j in range(100):
			if i == j:
				diag_list.append(array[j][i])
				diag_list2.append(reverse_array[j][i])
		sum_list.append(sum(diag_list))
		sum_list.append(sum(diag_list2))

	result = max(sum_list)
	print(f'#{tc} {result}')
