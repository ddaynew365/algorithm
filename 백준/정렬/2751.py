n = int(input())
list_ = []
for i in range(n):
    list_.append(int(input()))

list_ = list(set(list_))
list_.sort()

for i in list_:
    print(i)
