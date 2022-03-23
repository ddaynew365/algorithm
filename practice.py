x = '101'
y = '101'
z = '101'
n =5

while len(x) < n:
  x = '0' + x
 
print(x)

#zfill
y = y.zfill(5)
print(y)

#rjust
z = z.ljust(5, '0') 
print(z)
