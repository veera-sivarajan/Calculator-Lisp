import operator as op
var = {'x' : 1, 'y' : 2, '*': op.gt}

proc = var["*"]
print(proc(1, 2))
