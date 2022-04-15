n, k= map(int, input().split())
arr = list()
arr_reverse = list()
sqrt = int(n ** (1/2)) + 1

for num in range(1, sqrt):
  if n % num == 0:
    arr.append(num)
    if num != n // num:
      arr_reverse.append(n//num)
arr = arr + arr_reverse[::-1]
if len(arr) < k:
  print(0)
else:
  print(arr[k-1])