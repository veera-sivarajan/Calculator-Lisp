import operator as op
var = {'x' : 1, 'y' : 2, '*': op.gt, 'begin': lambda *x: x[-1]}

def func(*x):
  print(x)
args = [1, 2, [3, 4]]
print(*args)
