import math
n = int(input())

for i in range(2, int(math.sqrt(n))+3):
    if(i<2): continue
    while n % i == 0:
        print(i)
        n = n / i
if(n!=1):print(int(n))