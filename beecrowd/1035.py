a = int(input())
b = int(input())
c = int(input())
d = int(input())

cond1 = (b > c) and (d > a)
cond2 = (c + d) > (a + b)
cond3 = c > 0 and d > 0
cond4 = a % 2 == 0 # a eh par?

if cond1 and cond2 and cond3 and cond4:
  print('Valores aceitos')
else: 
  print('Valores nao aceitos')