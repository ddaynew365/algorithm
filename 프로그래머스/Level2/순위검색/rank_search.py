
from itertools import combinations

def solution(info, query):
  answer: list[int] = []
  qlist: dict = {}
  ilist: dict = dict()
  ilist[""] = []
  
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
      ilist[""].append(inf_score)
      for i in range(1, 5):
        combi = list(map(''.join, combinations(inf[:4], i)))
        print(j, combi)
        for t in combi:
          if t in ilist:
            ilist[t].append(inf_score)
          else:
            ilist[t] = [inf_score]
  for key in ilist.keys():
    ilist[key].sort()

  for command, standard in qlist.items():
    count = 0
    if command in ilist:
      count = len([i for i in ilist[command] if i>= standard])
      answer.append(count)
    else:
      answer.append(0)
              
  return answer
  
  
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]	
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info,query))