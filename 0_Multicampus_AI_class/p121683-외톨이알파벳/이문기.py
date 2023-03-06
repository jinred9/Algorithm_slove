def solution(input_string):
	length = len(input_string)
	answer_stack = []
	stack = []
	for i in range(length):
		if i == 0:
			stack.append(input_string[i])
		elif input_string[i] == input_string[i - 1]:
			continue
		elif input_string[i] not in stack:
			stack.append(input_string[i])
		elif input_string[i] in stack:
			answer_stack.append(input_string[i])
	answer = list(set([x for x in answer_stack]))
	answer.sort()
	if len(answer) == 0:
		answer = 'N'
	else:
		answer = ''.join(str(x) for x in answer)
	return answer

x = 'zbzbzasdasddd11zz33214'
print(solution(x))

