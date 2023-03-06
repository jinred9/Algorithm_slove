testcase = int(input())
for tc in range(1, testcase+1):
    sentence = input()
    stack = []
    for word in sentence:
        if len(stack) != 0 and stack[len(stack)-1] == word:
            stack.pop()
        else:
            stack.append(word)
    print(f"#{tc} {len(stack)}")