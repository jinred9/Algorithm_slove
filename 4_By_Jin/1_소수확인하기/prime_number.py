# def prime_number(x):
#     for pn in range(2, x + 1):
#         for pn_i in range(max(prime_list), pn + 1):
#             if pn % pn_i == 0 and pn != pn_i:
#                 break
#             elif pn % pn_i != 0 and pn not in prime_list:
#                 prime_list.append(pn)
#     if max(prime_list) == x:
#         z = str(x) + '는 소수이다.'
#     else:
#         z = str(x) + '는 소수가 아니다.'
#     return z


# x = 4
# prime_list = [1,2]
# print(prime_number(x))

n = 19
inp = 2**n-1
# 인터넷에서 찾은 방법===================================================================
prime_number = True
for i in range(2,inp):
	if inp % i != 0:
		pass
	else:
		prime_number = False
		break

if prime_number:
	print(inp, '소수이다.')
else: 
	print(inp, '소수가 아니다.')

# 인터넷에서 찾은 방법===================================================================
def solution1(x):
	for i in range(2, x):
		if x % i == 0:
			return False
	return True

if solution1(inp):
	print(inp, '소수이다.')
else:
	print(inp, '소수가 아니다.')
	
# 개선된 방식 인터넷에서 찾은 방법===================================================================
# ======================================약수의 성질을 이용======================================
# 모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이루는 것을 알 수 있다
# 예를 들어 16의 약수는 1, 2, 4, 8, 16이다
# 이때 2 X 8 = 16은 8 X 2 = 16과 대칭이다
# 따라서 우리는 특정한 자연수의 모든 약수를 찾을 때 가운데 약수(제곱근)까지만 확인하면 된다
# 예를 들어 16이 2로 나누어떨어진다는 것은 8로도 나누어떨어진다는 것을 의미한다
import math
def solution2(x):
	for i in range(2, int(math.sqrt(x))+1):
		if x % i == 0:
			return False
	return True

if solution2(inp):
	print(inp, '소수이다.')
else:
	print(inp, '소수가 아니다.')