Symbol = str
Number = (int, float)
Atom = (Symbol, Number)
List = list
Exp = (Atom, List)
Env = dict

def tokenize(line: str) -> list:
  return line.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(program: str) -> Exp:
  return readTokens(tokenize(program))
  
def readTokens(tokens: list) -> Exp:
  if len(tokens) == 0:
    raise SyntaxError('unexpected EOF')

  token = tokens.pop(0) #popping first element

  if token == '(':
    L = []
    while tokens[0] != ')':
      print("Inside while: " ,  tokens)
      L.append(readTokens(tokens))
    tokens.pop(0)
    return L
    
  '''
  elif token == ')':
    raise SyntaxError('unexpected )')

  else: 
    return atom(token)
  '''  

print(parse("(+ 1 (+ 2 3))"))
