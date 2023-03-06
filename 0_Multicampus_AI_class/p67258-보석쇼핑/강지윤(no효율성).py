def solution(gems):
    find = set(gems)
    numOfFinds = len(find)
    answer_dic = { i:[] for i in range(len(gems))}
    answer = []
    for start in range(len(gems)-numOfFinds+1):
        for end in range(start+numOfFinds-1,len(gems)):
            if start > len(gems)-numOfFinds:
                break;
            Frame = gems[start:end+1]
            if len(set(Frame)) == numOfFinds :
                answer_dic[end-start].append([start+1,end+1])
                break;


    for diff in range(len(answer_dic)):
        if answer_dic[diff]:
            sorted(answer_dic[diff])
            answer.append(answer_dic[diff][0])
            break;

    return(answer[0])





 





print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))

print(solution(["AA", "AB", "AC", "AA", "AC"]))

print(solution(["XYZ", "XYZ", "XYZ"]))

print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))