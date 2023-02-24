def solution(input_string):
    answer =''
    count =1
    check_dict = {}

    check_dict[input_string[0]] = []
    check = [input_string[0]]
    for txt in input_string:
        if txt not in check[-1]:
            check.append(txt)
            check_dict[txt] = []
    print(check)

    for txt in check:
        check_dict[txt].append(count)
        if len(check_dict[txt]) >= 2:
            answer += txt
    print(check_dict)
    answer = "".join(sorted(set(answer)))
    if answer:
        return answer
    else:
        return "N"



# def solution(input_string):
    # check = []
    # list = []
    # check_str = [0]
    # if len(input_string) != len(set(input_string)):
    #     for txt in input_string:
    #         if check and txt == check[-1]:
    #             check_str.append(check.pop())
    #
    #         elif check_str[-1] != txt:
    #             check.append(txt)
    #
    #
    #     for i in set(check_str):
    #         if check_str.count(i) >= 2:
    #             check.append(i)
    #
    #     result = ""
    #
    #     for string in sorted(set(check)):
    #
    #         result += string
    #
    #     return result
    # else:
    #     return 'N'




print(solution("edeaaabbccd"))
print(solution("eeddee"))
print(solution('string'))
print(solution('zbzbz'))