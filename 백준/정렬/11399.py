n = int(input())
list_ = list(map(int, input().split()))
answer = 0
list_.sort()

for i in range(n):
    wait = sum(list_[:i+1])
    answer += wait

print(answer)
