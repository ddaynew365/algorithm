def i(hi):
  if len(hi) == 1:
    return
  r = []
  r= hi
  i(hi[1:])
  print(r)
  
  

i([1,2,3])