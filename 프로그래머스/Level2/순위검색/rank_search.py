from itertools import permutations

def solution(info, query):
    answer: list[int] = []
    qlist: dict = {}
    ilist: list[list[str, int]] = []
    
    for i in query:
        problem = i.split(" and ")
        last = problem.pop()
        food, score = last.split(" ")
        problem += food
        problem = ''.join(problem)
        problem = problem.replace("-","");
        qlist[problem] = int(score)

    for j in info:
        inf = j.split(" ")
        inf_score = int(inf[4])
        inf_command = ''.join(map(''.join, permutations(inf[:4], 4)))
        ilist.append((inf_command, inf_score))

    for command, standard in qlist.items():
        count = 0
        for information, score in ilist:
            if command in information and score >= standard:
                count += 1
        answer.append(count)
                
    return answer