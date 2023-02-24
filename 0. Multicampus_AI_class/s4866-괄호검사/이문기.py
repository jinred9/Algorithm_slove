import sys
sys.stdin = open('input.txt')
T = int(input())
# 입력된 태스트 횟수 만큼 반복
for t in range(T):
	input_sentence = list(input())
	el = [] # extracted_list

	# 입력 값에서 괄호만 추출 하는 루프
	for k in input_sentence:
		if k == '(' or k == ')' or k == '[' or k == ']' or k == '{' or k == '}':
			el.append(k)

	# 인덱스, 태스트 할 리스트
	i = 0
	el_2 = el.copy()

	while True:
		# 1쌍의 괄호가 삭제 or 모두 검사후 삭제 될것이 없으면 루프 종료
		el_3 = el_2.copy()
		while True:
			if el_2[i] == '(':
				if el_2[i+1] == ')':
					del el_2[i]
					del el_2[i]
					i = 0
					break
				else:
					i += 1
			elif el_2[i] == '[':
				if el_2[i+1] == ']':
					del el_2[i]
					del el_2[i]
					i = 0
					break
				else:
					i += 1
			elif el_2[i] == '{':
				if el_2[i+1] == '}':
					del el_2[i]
					del el_2[i]
					i = 0
					break
				else:
					i += 1
			else:
				# 끝까지 검사후 삭제될게 없다면 종료
				if i+1 == int(len(el_2)) and el_2 == el:
					break
				else:
					i += 1
		# 1쌍도 삭제 되지 않는 다면 검사 종료
		if el_3 == el_2:
			break
		# 삭제후 원소가 0개 혹은 1개 일때 검사 종료
		elif len(el_2) == 0 or len(el_2) == 1:
			break

	# 원소가 0개면 1출력 , 아니면 0 출력
	if len(el_2) == 0:
		print(f'#{t+1} 1')
	else:
		print(f'#{t+1} 0')



