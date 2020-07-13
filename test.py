import operator as op
var = {'x' : 1, 'y' : 2, '*': op.gt, 'begin': lambda *x: x[-1]}

name = var['begin']
print(name("(begin (* 1 2))"))

x = ['begin', ['define', 'r', 10], ['*', 'r', 'r']]
def func(*y):
  print("y", y)
  print(y[0])

args = x[1:]
print(args)
print(*args)

rand = *args
func(*args)
print(rand)
