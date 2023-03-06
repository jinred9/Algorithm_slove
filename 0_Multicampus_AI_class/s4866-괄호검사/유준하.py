
testcase = int(input())
for tc in range(1, testcase+1):
    input_string = input()
    check = []
    for word in input_string:
        if word == '{' or word == '(':
            check.append(word)
        elif word == '}' or word == ')':
            if word == '}':
                if len(check) != 0 and check[len(check)-1] == '{':
                    check.pop()
                else:
                    check.append(word)
                    break
            elif word == ")":
                if len(check) != 0 and check[len(check)-1] == '(':
                    check.pop()
                else:
                    check.append(word)
                    break
    if not check:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
