# def find_size(graph, locate):
#     y, x = locate
#     need = 1
#     for i in range(2,6):
#         for row in range(i):
#             for column in range(i):
#                 newy, newx = y+row, x+column
#                 if newy < 0 or newy> 9 or newx < 0 or newx > 9 or graph[newy][newx] != 1:
#                     return need
#         need += 1
#     return need

# def cover(graph, locate, size):
#     y, x = locate
#     for row in range(size):
#         for column in range(size):
#             newy, newx = row + y, column + x
#             if newy < 0 or newy> 9 or newx < 0 or newx > 9:
#                 continue
#             graph[newy][newx] = 0
#     return graph
        
# def find_all_size(graph):
#     one_dict = dict()
#     for row in range(10):
#       for column in range(10):
#         if graph[row][column] == 1:
#             locate = [row, column]
#             size = find_size(graph, locate)
#             if size not in one_dict:
#                 one_dict[size] = [locate]
#             else:
#                 one_dict[size].append(locate)
#     return one_dict
    
# graph = [list(map(int,input().split(" "))) for _ in range(10)]
# remain_num = [5,5,5,5,5]
# one_dict = find_all_size(graph)
# answer = 0
# while one_dict and remain_num != [0,0,0,0,0]:
#     print(one_dict)
#     big_size = max(one_dict.keys())
#     if remain_num[big_size - 1] == 0 and big_size > 1:
#         temp = one_dict[big_size]
#         del one_dict[big_size]
#         big_size = max(one_dict.keys())
#         one_dict[big_size] += temp  
#     if big_size == 1 and remain_num[0] == 0:
#         answer = -1
#         break
#     locate = one_dict[big_size][0]
#     graph = cover(graph, locate,big_size)
#     remain_num[big_size-1] -= 1
#     one_dict = find_all_size(graph)
    

# if answer != -1:
#     for i in range(5):
#         answer += 5 - remain_num[i]
# print(answer) 
# # 그리디 형식으로 풀었지만 내가 선정한 가장 큰 색종이부터 사용하게 된다는 조건이 최선이 아니므로 그리디는 실패하였다
# # 따라서 완전탐색을 위해 재귀를 사용해야 했다(dfs)
answer = 10000
def posible_num(graph, locate):
    y, x = locate
    pos = [1]
    need = 1
    for i in range(2,6):
        for row in range(i):
            for column in range(i):
                newy, newx = y+row, x+column
                if newy < 0 or newy> 9 or newx < 0 or newx > 9 or graph[newy][newx] != 1:
                    return pos
        need += 1
        pos.append(need)
    return pos   
def cover(graph, size, remain, locate):
  
    y, x = locate
    remain[size] -= 1
    for row in range(size):
        for column in range(size):
            newy, newx = row + y, column + x
            if newy < 0 or newy> 9 or newx < 0 or newx > 9:
                continue
            graph[newy][newx] = 0
    return [graph, remain]

def recursion(graph, remain):
    print()
    if 1 not in [val for rows in graph for val in rows]:
        global answer
        cur =  25 - sum(remain)
        if answer > cur:
            answer = cur
        return
    if remain == [0,0,0,0,0,0]:
        return
    
    for row in range(10):
        for column in range(10):
            if graph[row][column] == 1:
                locate =[row,column]
                pos = posible_num(graph, locate)
                for size in pos[::-1]:
                    print(size)
                    if remain[size] == 0:
                        continue
                    new_graph, new_remain = cover([[graph[i][j] for j in range(10)]for i in range(10)], size, remain[:], locate)
                    recursion(new_graph,new_remain)
            
graph = [list(map(int,input().split(" "))) for _ in range(10)]
remain = [0, 5,5,5,5,5]
recursion(graph,remain)
if answer == 10000:
    answer = -1
print(answer)
